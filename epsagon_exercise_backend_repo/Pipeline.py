from aws_cdk import (
    aws_codepipeline,
    aws_codepipeline_actions,
    core,
    aws_ecr,
    aws_codebuild,
    aws_ssm,
    aws_iam as iam,
    aws_codecommit,
    aws_ecs_patterns as ecs_patterns,
    aws_ecs as ecs,
    aws_ec2 as ec2,
)


class Pipeline(core.Stack):
    def __init__(self, app: core.App, id: str, props, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        ecr = aws_ecr.Repository(
            self, "ECR",
            repository_name=f"{props['namespace']}",
            removal_policy=core.RemovalPolicy.DESTROY
        )

        codecommit_repo = aws_codecommit.Repository.from_repository_name(self, "ImportedRepo",
                                                          f"{props['namespace']}")

        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)  # default is all AZs in region

        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        cluster.add_capacity("DefaultAutoScalingGroup",
                             instance_type=ec2.InstanceType("t2.micro"))

        execution_role = iam.Role(self,
                                  "ecs-devops-sandbox-execution-role",
                                  assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                                  role_name="ecs-devops-sandbox-execution-role")
        execution_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ]
        ))

        task_definition = ecs.FargateTaskDefinition(self,
                                                    "spans-server-task-definition",
                                                    execution_role=execution_role,
                                                    family="spans-server-task-definition")

        # stack = core.Stack(app, "aws-ecs-integ-ecs")

        # task_definition = ecs.Ec2TaskDefinition(
        #     self, "TaskDef",
        #     placement_constraints=[
        #         ecs.PlacementConstraint.distinct_instances()
        #     ]
        # )

        # container = task_definition.add_container(
        #     "spans-server",
        #     image=ecs.ContainerImage.from_registry(ecr.repository_uri)
        # )

        container = task_definition.add_container(
            "spans-server",
            image=ecs.ContainerImage.from_registry("nginx:latest"),
            memory_limit_mib=256,
        )

        # port_mapping = ecs.PortMapping(
        #     container_port=80,
        #     host_port=8080,
        #     protocol=ecs.Protocol.TCP
        # )
        # container.add_port_mappings(port_mapping)

        # Create the ECS Service
        service = ecs.FargateService(self,
                                     "spans-server-service",
                                     cluster=cluster,
                                     task_definition=task_definition,
                                     service_name="spans-server-service")

        # service = ecs.Ec2Service(
        #     self, "Service",
        #     cluster=cluster,
        #     task_definition=task_definition,
        # )

        # service.add_placement_strategies(
        #     ecs.PlacementStrategy.packed_by(ecs.BinPackResource.MEMORY))
        # service.add_placement_strategies(
        #     ecs.PlacementStrategy.spread_across(
        #         ecs.BuiltInAttributes.AVAILABILITY_ZONE))

        cb_docker_build = aws_codebuild.PipelineProject(
            self, "DockerBuild",
            project_name=f"{props['namespace']}-Docker-Build",
            build_spec=aws_codebuild.BuildSpec.from_source_filename(
                filename='./epsagon_exercise_backend_repo/pipeline_delivery/docker_build_buildspec.yml'),
            # build_spec=aws_codebuild.BuildSpec.from_object(
            #     {
            #
            #     }
            # ),
            environment=aws_codebuild.BuildEnvironment(
                privileged=True,
            ),
            # pass the ecr repo uri into the codebuild project so codebuild knows where to push
            environment_variables={
                'ecr': aws_codebuild.BuildEnvironmentVariable(
                    value=ecr.repository_uri),
                'tag': aws_codebuild.BuildEnvironmentVariable(
                    value='spans-server')
            },
            description='Pipeline for CodeBuild',
            timeout=core.Duration.minutes(60),
        )

        # cb_docker_deploy = aws_codebuild.PipelineProject(
        #     self, "DockerBuild",
        #     project_name=f"{props['namespace']}-Docker-Deploy",
        #     build_spec=aws_codebuild.BuildSpec.from_source_filename(
        #         filename='pipeline_delivery/docker_deploy_buildspec.yml'),
        #     environment=aws_codebuild.BuildEnvironment(
        #         privileged=True,
        #     ),
        #     # pass the ecr repo uri into the codebuild project so codebuild knows where to push
        #     environment_variables={
        #         'ecr': aws_codebuild.BuildEnvironmentVariable(
        #             value=ecr.repository_uri),
        #         'tag': aws_codebuild.BuildEnvironmentVariable(
        #             value='spans-server')
        #     },
        #     description='Pipeline for CodeBuild',
        #     timeout=core.Duration.minutes(60),
        # )

        ecr.grant_pull_push(cb_docker_build)

        core.CfnOutput(
            self, "ECRURI",
            description="ECR URI",
            value=ecr.repository_uri,
        )

        # define the s3 artifact
        source_output = aws_codepipeline.Artifact(artifact_name='source')
        # define the pipeline
        pipeline = aws_codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name=f"{props['namespace']}",
            # artifact_bucket=props['bucket'],
            stages=[
                aws_codepipeline.StageProps(
                    stage_name="Source",
                    actions=[
                        aws_codepipeline_actions.CodeCommitSourceAction(
                            action_name="CodeCommit_Source",
                            repository=codecommit_repo,
                            output=source_output)]),
                aws_codepipeline.StageProps(
                    stage_name='Build',
                    actions=[
                        aws_codepipeline_actions.CodeBuildAction(
                            action_name='DockerBuildImages',
                            input=source_output,
                            project=cb_docker_build,
                            run_order=1,
                        )
                    ]
                ),
                aws_codepipeline.StageProps(
                    stage_name='Deploy',
                    actions=[
                        aws_codepipeline_actions.EcsDeployAction(
                            action_name="DeployAction",
                            service=service,
                            # if your file is called imagedefinitions.json,
                            # use the `input` property,
                            # and leave out the `imageFile` property
                            input=source_output,
                            # if your file name is _not_ imagedefinitions.json,
                            # use the `imageFile` property,
                            # and leave out the `input` property
                            # image_file=server_build_output.at_path("imageDef.json"),
                            deployment_timeout=core.Duration.minutes(60)
                        )
                    ]
                )
            ])

        # cfn output
        core.CfnOutput(
            self, "PipelineOut",
            description="Pipeline",
            value=pipeline.pipeline_name
        )
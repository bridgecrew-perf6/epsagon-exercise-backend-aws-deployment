from aws_cdk import (
    aws_s3 as aws_s3,
    aws_ecr,
    aws_codebuild,
    aws_ssm,
    aws_ecs_patterns as ecs_patterns,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    core,
)

class Base(core.Stack):
    def __init__(self, app: core.App, id: str, props, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        # pipeline requires versioned bucket
        # bucket = aws_s3.Bucket(
        #     self, "SourceBucket",
        #     bucket_name=f"{props['namespace'].lower()}-{core.Aws.ACCOUNT_ID}",
        #     versioned=True,
        #     removal_policy=core.RemovalPolicy.DESTROY)
        # # ssm parameter to get bucket name later
        # bucket_param = aws_ssm.StringParameter(
        #     self, "ParameterB",
        #     parameter_name=f"{props['namespace']}-bucket",
        #     string_value=bucket.bucket_name,
        #     description='cdk pipeline bucket'
        # )
        # ecr repo to push docker container into
        ecr = aws_ecr.Repository(
            self, "ECR",
            repository_name=f"{props['namespace']}",
            removal_policy=core.RemovalPolicy.DESTROY
        )

        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)  # default is all AZs in region

        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        # fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
        #     self, "MyFargateService",
        #     cluster=cluster,  # Required
        #     # cpu=512,  # Default is 256
        #     # desired_count=6,  # Default is 1
        #     task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
        #         image=ecs.ContainerImage.from_registry(
        #             "$ecr:$tag")),
        #     # memory_limit_mib=2048,  # Default is 512
        #     public_load_balancer=True)  # Default is False

        # codebuild project meant to run in pipeline
        cb_docker_build = aws_codebuild.PipelineProject(
            self, "DockerBuild",
            project_name=f"{props['namespace']}-Docker-Build",
            build_spec=aws_codebuild.BuildSpec.from_source_filename(
                filename='pipeline_delivery/docker_build_buildspec.yml'),
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
        # codebuild iam permissions to read write s3
        # bucket.grant_read_write(cb_docker_build)

        # codebuild permissions to interact with ecr
        ecr.grant_pull_push(cb_docker_build)

        core.CfnOutput(
            self, "ECRURI",
            description="ECR URI",
            value=ecr.repository_uri,
        )
        # core.CfnOutput(
        #     self, "S3Bucket",
        #     description="S3 Bucket",
        #     value=bucket.bucket_name
        # )

        self.output_props = props.copy()
        # self.output_props['bucket']= bucket
        self.output_props['cb_docker_build'] = cb_docker_build
        # self.output_props['fargate_service'] = fargate_service

    # pass objects to another stack
    @property
    def outputs(self):
        return self.output_props

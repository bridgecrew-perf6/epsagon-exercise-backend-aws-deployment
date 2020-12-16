from aws_cdk import (core, aws_codebuild as codebuild,
                     aws_codecommit as codecommit,
                     aws_codepipeline as codepipeline,
                     aws_codepipeline_actions as codepipeline_actions,
                     aws_ecs as ecs,
                     aws_ec2 as ec2,
                     aws_ecs_patterns as ecs_patterns,
                     aws_lambda as lambda_)

class EpsagonExerciseBackendRepoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, repo_name: str = None,
                 lambda_code: lambda_.CfnParametersCode = None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        code = codecommit.Repository.from_repository_name(self, "ImportedRepo",
                                                          repo_name)

        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)  # default is all AZs in region

        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "MyFargateService",
            cluster=cluster,  # Required
            # cpu=512,  # Default is 256
            # desired_count=6,  # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
               image=ecs.ContainerImage.from_registry(
                   "$REPOSITORY_URI")),
            # memory_limit_mib=2048,  # Default is 512
            public_load_balancer=True)  # Default is False

        cdk_build = codebuild.PipelineProject(
            self, "CdkBuild",
            build_spec=codebuild.BuildSpec.from_object(dict(
                version="0.2",
                phases=dict(
                    install=dict(
                        commands=[
                            "npm install aws-cdk",
                            "npm update",
                            "python -m pip install -r requirements.txt"
                        ]),
                    build=dict(commands=[
                        "npx cdk synth -o dist"])),
                artifacts={
                    "base-directory": "dist",
                    "files": [
                        "LambdaStack.template.json"]},
                environment=dict(buildImage=
                                 codebuild.LinuxBuildImage.STANDARD_2_0))))

        spans_build = codebuild.PipelineProject(
             self,
             'ServerBuild',
             build_spec=codebuild.BuildSpec.from_object(dict(
                 version="0.2",
                 phases={
                     "install": {
                         "runtime-versions": {
                             "python": "3.9"
                         },
                         "commands": [
                             "pip3 install -r requirements.txt"
                         ]
                     },
                     "pre_build": {
                         "commands": [
                             "aws --version",
                             "$(aws ecr get-login --region ${WS_DEFAULT_REGION} --no-include-email | sed 's|https://||')",
                             'COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)',
                             'IMAGE_TAG=${COMMIT_HASH:=latest}'
                         ]
                     },
                     "build": {
                         "commands": [
                            'docker build -t $REPOSITORY_URI:latest .',
                            'docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:IMAGE_TAG'
                        ]
                     },
                     "post_build": {
                         "commands": [
                             'docker push $REPOSITORY_URI:latest .',
                            'docker push $REPOSITORY_URI:$IMAGE_TAG'
                         ]
                     }
                 },
             )))

        source_output = codepipeline.Artifact()
        cdk_build_output = codepipeline.Artifact("CdkBuildOutput")
        spans_build_output = codepipeline.Artifact("ServerBuildOutput")

        # lambda_location = lambda_build_output.s3_location

        codepipeline.Pipeline(
            self, "Pipeline",
            stages=[
                codepipeline.StageProps(
                stage_name="Source",
                actions=[
                    codepipeline_actions.CodeCommitSourceAction(
                        action_name="CodeCommit_Source",
                        repository=code,
                        output=source_output)]),
                    codepipeline.StageProps(
                        stage_name="Build",
                        actions=[
                            codepipeline_actions.CodeBuildAction(
                                action_name="CDK_Build",
                                project=cdk_build,
                                input=source_output,
                                outputs=[cdk_build_output]),
                            codepipeline_actions.CodeBuildAction(
                                action_name="Spans_Build",
                                project=spans_build,
                                input=source_output,
                                outputs=[spans_build_output])]),
                    codepipeline.StageProps(
                        stage_name="Deploy",
                        actions=[
                            codepipeline_actions.EcsDeployAction(
                                action_name="DeployAction",
                                service=fargate_service,
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
                    )])

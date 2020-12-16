from aws_cdk import (core, aws_codebuild as codebuild,
                     aws_codecommit as codecommit,
                     aws_codepipeline as codepipeline,
                     aws_codepipeline_actions as codepipeline_actions,
                     aws_ecs as ecs,
                     aws_lambda as lambda_)

class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, repo_name: str=None,
                 lambda_code: lambda_.CfnParametersCode=None, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        code = codecommit.Repository.from_repository_name(self, "ImportedRepo",
                  repo_name)

        cdk_build = codebuild.PipelineProject(self, "CdkBuild",
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

        # lambda_build = codebuild.PipelineProject(self, 'LambdaBuild',
        #                 build_spec=codebuild.BuildSpec.from_object(dict(
        #                     version="0.2",
        #                     phases=dict(
        #                         install=dict(
        #                             commands=[
        #                                 "cd lambda",
        #                                 "npm install",
        #                                 "npm install typescript"]),
        #                         build=dict(
        #                             commands=[
        #                                 "npx tsc index.ts"])),
        #                     artifacts={
        #                         "base-directory": "lambda",
        #                         "files": [
        #                             "index.js",
        #                             "node_modules/**/*"]},
        #                     environment=dict(buildImage=
        #                         codebuild.LinuxBuildImage.STANDARD_2_0))))

        server_build = codebuild.PipelineProject(self, 'ServerBuild',
                                                 build_spec=codebuild.BuildSpec.from_object(dict(
                                                     version="0.2",
                                                     phases=dict(
                                                        install = dict(
                                                            python = "3.8"
                                                        ),
                                                         commands = [
                                                             "pip3 install -r requirements.txt"
                                                         ],
                                                     ),
                                                     build = dict(
                                                         commands = [
                                                             'docker build -t $REPOSITORY_URI:latest .',
                                                             'docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:IMAGE_TAG'
                                                         ]
                                                     ),
                                                     post_build = dict(
                                                         commands = [
                                                             'docker push $REPOSITORY_URI:latest .',
                                                             'docker push $REPOSITORY_URI:$IMAGE_TAG'
                                                         ]
                                                     )
                                                 )))

        source_output = codepipeline.Artifact()
        cdk_build_output = codepipeline.Artifact("CdkBuildOutput")
        server_build_output = codepipeline.Artifact("ServerBuildOutput")

        # lambda_location = lambda_build_output.s3_location

        codepipeline.Pipeline(self, "Pipeline",
            stages=[
                codepipeline.StageProps(stage_name="Source",
                    actions=[
                        codepipeline_actions.CodeCommitSourceAction(
                            action_name="CodeCommit_Source",
                            repository=code,
                            output=source_output)]),
                codepipeline.StageProps(stage_name="Build",
                    actions=[
                        # codepipeline_actions.CodeBuildAction(
                        #     action_name="Lambda_Build",
                        #     project=lambda_build,
                        #     input=source_output,
                        #     outputs=[lambda_build_output]),
                        codepipeline_actions.CodeBuildAction(
                            action_name="CDK_Build",
                            project=cdk_build,
                            input=source_output,
                            outputs=[cdk_build_output])]),
                # codepipeline.StageProps(
                #     stage_name="Deploy",
                #     actions=[
                #         codepipeline_actions.EcsDeployAction(
                #             action_name="DeployAction",
                #             service=ecs.Ec2Service(self, ),
                #             # if your file is called imagedefinitions.json,
                #             # use the `input` property,
                #             # and leave out the `imageFile` property
                #             input=server_build_output,
                #             # if your file name is _not_ imagedefinitions.json,
                #             # use the `imageFile` property,
                #             # and leave out the `input` property
                #             # image_file=server_build_output.at_path("imageDef.json"),
                #             deployment_timeout=core.Duration.minutes(60)
                #         )
                #
                #     ]
                # )
                # codepipeline.StageProps(stage_name="Deploy",
                #     actions=[
                #         codepipeline_actions.CloudFormationCreateUpdateStackAction(
                #             action_name="Lambda_CFN_Deploy",
                #             template_path=cdk_build_output.at_path(
                #                 "LambdaStack.template.json"),
                #             stack_name="LambdaDeploymentStack",
                #             admin_permissions=True)
                #             # parameter_overrides=dict(
                #             #     lambda_code.assign(
                #             #         bucket_name=lambda_location.bucket_name,
                #             #         object_key=lambda_location.object_key,
                #             #         object_version=lambda_location.object_version)),
                #             # extra_inputs=[lambda_build_output])
                #     ])
                ]
            )
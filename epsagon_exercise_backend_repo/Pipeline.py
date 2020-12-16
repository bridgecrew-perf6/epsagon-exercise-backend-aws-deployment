from aws_cdk import (
    aws_codepipeline,
    aws_codepipeline_actions,
    aws_ssm,
    core,
)


class Pipeline(core.Stack):
    def __init__(self, app: core.App, id: str, props, **kwargs) -> None:
        super().__init__(app, id, **kwargs)
        # define the s3 artifact
        source_output = aws_codepipeline.Artifact(artifact_name='source')
        # define the pipeline
        pipeline = aws_codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name=f"{props['namespace']}",
            # artifact_bucket=props['bucket'],
            stages=[
                # aws_codepipeline.StageProps(
                #     stage_name='Source',
                #     actions=[
                #         aws_codepipeline_actions.S3SourceAction(
                #             bucket=props['bucket'],
                #             bucket_key='source.zip',
                #             action_name='S3Source',
                #             run_order=1,
                #             output=source_output,
                #             trigger=aws_codepipeline_actions.S3Trigger.POLL
                #         ),
                #     ]
                # ),
                aws_codepipeline.StageProps(
                    stage_name='Build',
                    actions=[
                        aws_codepipeline_actions.CodeBuildAction(
                            action_name='DockerBuildImages',
                            input=source_output,
                            project=props['cb_docker_build'],
                            run_order=1,
                        )
                    ]
                ),
                # aws_codepipeline.StageProps(
                #     stage_name="Deploy",
                #     actions=[
                #         aws_codepipeline_actions.EcsDeployAction(
                #             action_name="DeployAction",
                #             service=props['fargate_service'],
                #             # if your file is called imagedefinitions.json,
                #             # use the `input` property,
                #             # and leave out the `imageFile` property
                #             input=source_output,
                #             # if your file name is _not_ imagedefinitions.json,
                #             # use the `imageFile` property,
                #             # and leave out the `input` property
                #             # image_file=server_build_output.at_path("imageDef.json"),
                #             deployment_timeout=core.Duration.minutes(60)
                #         )
                #
                #     ]
                # )
            ]

        )
        # give pipelinerole read write to the bucket
        # props['bucket'].grant_read_write(pipeline.role)

        #pipeline param to get the
        pipeline_param = aws_ssm.StringParameter(
            self, "PipelineParam",
            parameter_name=f"{props['namespace']}-pipeline",
            string_value=pipeline.pipeline_name,
            description='cdk pipeline bucket'
        )
        # cfn output
        core.CfnOutput(
            self, "PipelineOut",
            description="Pipeline",
            value=pipeline.pipeline_name
        )
#!/usr/bin/env python3

from aws_cdk import core

# from epsagon_exercise_backend_repo.epsagon_exercise_backend_repo_stack import EpsagonExerciseBackendRepoStack
# from epsagon_exercise_backend_repo.pipeline_stack import PipelineStack

from Base import Base
from Pipeline import Pipeline

props = {'namespace': 'spans-server-ns'}
app = core.App()

# stack for ecr, bucket, codebuild
base = Base(app, f"{props['namespace']}-base", props)

# pipeline stack
pipeline = Pipeline(app, f"{props['namespace']}-pipeline", base.outputs)
pipeline.add_dependency(base)
app.synth()

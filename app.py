#!/usr/bin/env python3

from aws_cdk import core

from epsagon_exercise_backend_repo.epsagon_exercise_backend_repo_stack import EpsagonExerciseBackendRepoStack
from epsagon_exercise_backend_repo.pipeline_stack import PipelineStack

app = core.App()
EpsagonExerciseBackendRepoStack(app, "epsagon-exercise-backend-repo")
PipelineStack(app, 'PipelineDeployingServerStack',
              repo_name="epsagon-exercise-backend-repo")

app.synth()

#!/usr/bin/env python3

from aws_cdk import core

from my_first_stack.my_first_stack_stack import MyFirstStackStack


app = core.App()
MyFirstStackStack(app, "my-first-stack",env=core.Environment(region="eu-central-1",account="521261446919"))

app.synth()

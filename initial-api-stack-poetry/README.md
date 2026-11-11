
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project uses [Poetry](https://python-poetry.org/) for dependency management.

## Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup

Install the project dependencies:

```
$ poetry install
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ poetry run cdk synth
```

To add additional dependencies, for example other CDK libraries, use:

```
$ poetry add <package>
```

For development dependencies:

```
$ poetry add --group dev <package>
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

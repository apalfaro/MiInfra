#!/usr/bin/env python
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace
from constructs import Construct

from imports.aws.provider import AwsProvider
from imports.aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, 'aws', region='us-east-2')

        # define resources here
        self.MyBucket = S3Bucket(
            self,
            id_="MyBucket",
            bucket="aalfaro-my-bucket"
        )


app = App()
stack = MyStack(app, "MiS3")
CloudBackend(stack,
             hostname='app.terraform.io',
             organization='example-org-bc86fc',
             workspaces=NamedCloudWorkspace('MiS3')
             )

app.synth()

#!/usr/bin/env python
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace
from constructs import Construct

from imports.aws.provider import AwsProvider
from imports.aws.s3_bucket import S3Bucket, S3BucketServerSideEncryptionConfiguration, \
    S3BucketServerSideEncryptionConfigurationRule


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, 'aws', region='us-east-2')

        # define resources here
        self.MyBucket = S3Bucket(
            self,
            id_="MyBucket",
            bucket="aalfaro-my-bucket",
            server_side_encryption_configuration=S3BucketServerSideEncryptionConfiguration(self,
                                                                                           rule=S3BucketServerSideEncryptionConfigurationRule(
                                                                                               "bucket_key_enabled")
                                                                                           )
        )

        app = App()
        stack = MyStack(app, "MiS3")
        CloudBackend(stack,
                     hostname='app.terraform.io',
                     organization='example-org-bc86fc',
                     workspaces=NamedCloudWorkspace('MiS3')
                     )

        app.synth()

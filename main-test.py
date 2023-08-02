import pytest
from cdktf import Testing, TerraformStack


# The tests below are example tests, you can find more information at
# https://cdk.tf/testing


class TestMain:

    stack = TerraformStack(Testing.app(), "stack")
    synthesized = Testing.synth(stack)

    def test_should_contain_bucket(self):
        assert Testing.to_have_resource(self.synthesized, "MyBucket")

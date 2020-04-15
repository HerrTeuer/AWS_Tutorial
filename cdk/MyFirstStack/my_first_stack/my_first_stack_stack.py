from aws_cdk import (
    core,
    aws_s3 as s3
)


class MyFirstStackStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(
            self,
            "sitebucket",
            bucket_name="asdadfafadfedasfsgs-mybucket-123435",
            public_read_access=True
        )

        core.CfnOutput(self,"sitebucketname",value=bucket.bucket_name)

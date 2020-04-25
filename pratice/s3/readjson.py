import json
import boto3

s3 = boto3.resource("s3")
bucket = "mytempfileforcloudwatchmetrics"
key="configuration/test/config.json"

response = s3.Object(bucket,key).get()
body=response["Body"].read()
jsonfile = json.loads(body)
#print(jsonfile)

s3_client = boto3.client("s3")
response = s3_client.list_objects_v2(
    Bucket= bucket,
    Prefix="2020-04-16/",
)
#print(response)
contents = response["Contents"]
filelist = []
for content in contents:
    filelist.append(content["Key"])

print(filelist)

import json
import boto3

s3 = boto3.resource("s3")
bucket = "mytempfileforcloudwatchmetrics"
key="2020-04-16/EC2-CPUUtilization-i-08be9e7184ce17f36-2020-04-16.csv"

response = s3.Object(bucket,key).get()
body=response["Body"].read()
print(body)
jsonfile = json.load(body)

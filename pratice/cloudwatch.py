from datetime import datetime,date,timedelta
import boto3

# parameter
startTime = datetime.utcnow() - timedelta(seconds=600)
endTime = datetime.utcnow()

cloudwatch = boto3.client('cloudwatch',region_name='eu-central-1')

logs = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName = "CPUUtilization",
    Dimensions = [
        {
            "Name" : "InstanceId",
            "Value" : "i-08be9e7184ce17f36"
        }
    ],
    StartTime = startTime,
    EndTime = endTime,
    Period = 300,
    Statistics = ["Average"]
)
print("ec2 metrics")
print(logs['Datapoints'])



logs = cloudwatch.get_metric_statistics(
    Namespace="AWS/EBS",
    MetricName = "VolumeReadOps",
    Dimensions = [
        {
            "Name" : "VolumeId",
            "Value" : "vol-004e90b6a66a4dfc2"
        }
    ],
    StartTime = startTime,
    EndTime = endTime,
    Period = 300,
    Statistics = ["Average"]
)

print("ebs metrics")
print(logs['Datapoints'])
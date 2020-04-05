## 1 aws cli 账户设置 credential config
# aws configure


## 2 设置正在运行的ec2实例的id,和账户号
$myInstanceID = "i-05b4c29b8503e700c"
$productionAccount = "xxxxxxxxxx"
$developmentAccount = "xxxxxxxxxx"

## 3 停止ec2实例
aws ec2 stop-instances --instance-ids $myInstanceID

# aws ec2 start-instances --instance-ids $myInstanceID

## 4 创建AMI
$myTestImageID = $(aws ec2 create-image --instance-id $myInstanceID --name "mytestAMI1" --description "AMI created by script")

## 5 AMI共享设置，发布到生产账户和开发账户
aws ec2 modify-image-attribute --image-id $myTestImageID --launch-permission "Add=[{UserId=$productionAccount}]"
aws ec2 modify-snapshot-attribute --snapshot-id snap-1234567890abcdef0 --attribute createVolumePermission --operation-type add --user-ids $productionAccount

## 6 查看成功与否



## 7 删除所有
#!/usr/bin/env python3 
import boto3

aws_region = ["us-east-1"]
for region in aws_region:
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.all()
    for instance in instances:
        print("Instance ID:", instance.instance_id)
        if len(instance.tags) > 0:
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    print(f'Instance Name:    {tag["Value"]}')  
        print("Instance State:", instance.state["Name"])
        print("Key_name:", instance.key_name)
        print("Launch Time:", instance.launch_time)
        print("Public IP Address:", instance.public_ip_address)
        print("Private IP Address:", instance.private_ip_address)
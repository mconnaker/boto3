#!/usr/bin/env python3 
import io
import boto3

with io.open("ec2_tags.csv", "r", encoding="utf-8") as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
for row in data:
    rows=row.split(",")
    region = "{}".format(rows[0])
    ec2 = boto3.resource('ec2', region_name=region)
    for instance in ec2.instances.all():
        if instance.id == rows[1]:
            print("Adding tag to", rows[1])
            ec2.create_tags(Resources=[rows[1]], Tags=[{'Key':rows[2], 'Value':rows[3]}])
        else:
            print("Error, Instance", rows[1],"does not exist in", rows[0])
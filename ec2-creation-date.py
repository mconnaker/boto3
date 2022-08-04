#!/usr/bin/env python3 
import boto3
from datetime import datetime 

aws_region = [""]
for region in aws_region:
    ec2 = boto3.resource('ec2', region_name=region)
    volume = ec2.volumes.all()
    print("Starting in ", region)
    print('*******************************')
    for v in volume:
        for a in v.attachments:
            print("Instance Id      ", a['InstanceId'])
            instances = ec2.instances.filter(
                InstanceIds=[a['InstanceId'],
                ],
            )  
            try:
                for instance in instances:
                    for device in instance.block_device_mappings:
                        if device['DeviceName']==instance.root_device_name:
                            if v.id ==device['Ebs']['VolumeId']:
                                print("AWS Region:      ", region)
                                print("Volume Status:   ", v.state)
                                print("Volume Creation: ", v.create_time.strftime("%Y-%m-%d %H:%M:%S"))
                                print("Root Volume:     ", device['Ebs']['VolumeId'])
                                if len(instance.tags) > 0:
                                    for tag in instance.tags:
                                        if tag['Key'] == 'Name':
                                            print(f'Instance Name:    {tag["Value"]}')    
                            if v.id !=device['Ebs']['VolumeId']:
                                print()
                            else: next(iter)
            except TypeError as te:
                print()
        print()
    print('*******************************')
    print("Finished with Region")
    print()
print("End of List")
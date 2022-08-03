# Introduction
Boto3 is a Python package that provides interfaces to Amazon Web Services. This respository contains various scripts that can be used to get information from AWS.

## Scripts

### EC2 Creation
In AWS there is no way to pull or retrieve the when an ec2 instance was first created. AWS does not store this information in metadata. The launch-time only gives approximation of when the ec2 instance was last stop/start or rebooted. However, there is a work around. Root Device EBS Volumes are generally never replaced after ec2 instance is created. Therefore, one can approximate when the ec2 instance was most likely spun up by retrieving the creation date of the EBS Volume
<br>
<br>
This script is designed to retrieve the creation date of the root device EBS Volume and identify whom it is attached to.
<br>
<br>
Data retrieved:
- AWS Region:
- Volume Status: (in-use)
- Volume Type: (Root)
- Volume ID:
- Volume Creation Date:
- Attached To
    - Instance ID
    - Instance Name
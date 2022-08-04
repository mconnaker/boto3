# Introduction
Boto3 is a Python package that provides interfaces to Amazon Web Services. This respository contains various scripts that can be used to get information from AWS.

## Scripts

### EC2 Creation
In AWS there isn't a way to retrieve when an ec2 instance was first created. AWS does not store this in metadata. The launch-time only gives approximation of when an ec2 instance was last stop/start or rebooted. 
<br><br>
However, there is a work around. Root Device EBS Volumes generally are not replaced after ec2 instance creation. Therefore, one can approximate when the ec2 instance was likely spun up by retrieving the creation date of the root device EBS Volume.
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

<br>
<br>

### List Ec2 Instance
This script is designed to retrieve a list of ec2 instances in a region of your aws account. You can configure region to look for multiple regions.

Data retrieved:
- Instance ID
- Instance Name
- Instance State
- Key_name
- Launch Time
- Public IP Address
- Private IP Address
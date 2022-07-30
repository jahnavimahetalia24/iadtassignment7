import boto3
ec2 = boto3.resource('ec2')

#Import boto3 : It is used to import boto3.
#ec2 = boto3.resource(‘ec2’) : The resource or service I am using with boto3 is ec2.
#instances = ec2.create_instances : It will create an EC2 instance.
#ImageId : It is an Amazon Machine Image (AMI) id. When we create an EC2 instance the first step is to select AMI id. 
#And it changes according to the region you choose. Here I am using ap-south-1 (Mumbai Region). 

def create_launch_configuration(assign):
    USER_DATA = '''
    #!/bin/bash
sudo apt update
sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
    '''
    
    launch = assign.create_launch_configuration(
        LaunchConfigurationName="jahnavi24",
        KeyName="iadtassignment7",
        UserData=USER_DATA,
        ImageId='ami-052efd3df9dad4825',
        InstanceType='t2.nano'
    )
    print(launch)
    create_ec2_instances(assign, launch)

def create_ec2_instances(assign):
    response = assign.create_auto_scaling_group(
        AutoScalingGroupName="Autoscaling_Group",
        MinSize=2,
        MaxSize=3,
        LaunchConfigurationName="jahnavi24",
        AvailabilityZones=['us-east-1a'],
        Tags=[
        {
            'ResourceId': 'Autoscaling_Group',
            'Key': 'Name',
            'Value': 'Name',
            'PropagateAtLaunch': True
        },
    ],
    )
    print(response)

assign = boto3.client('autoscaling',region_name='us-east-1')
create_launch_configuration(assign)
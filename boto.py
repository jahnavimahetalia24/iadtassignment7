import boto3
ec2 = boto3.resource('ec2')

#Import boto3 : It is used to import boto3.
#ec2 = boto3.resource(‘ec2’) : The resource or service I am using with boto3 is ec2.
#instances = ec2.create_instances : It will create an EC2 instance.
#ImageId : It is an Amazon Machine Image (AMI) id. When we create an EC2 instance the first step is to select AMI id. 
#And it changes according to the region you choose. 

assign = boto3.client('autoscaling',region_name='us-east-1') #launch config for instances, in our case apache setup
USER_DATA = '''#!/bin/bash 
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo rm -rf iadtassignment7
git clone https://github.com/jahnavimahetalia24/iadtassignment7.git
sudo rm -rf /var/www/html/index.html
sudo mv iadtassignment7/index.html /var/www/html
sudo systemctl enable apache2
sudo systemctl restart apache2
''' 
launch = assign.create_launch_configuration( 
    LaunchConfigurationName="jahnavi", #launch config name
    KeyName="iadtautoscaling", #group name
    UserData=USER_DATA,
    ImageId='ami-052efd3df9dad4825', #image id - Ubuntu in this case
    InstanceType='t2.nano' #min req for an instance 
)
print(launch)
res = assign.create_auto_scaling_group(
    AutoScalingGroupName="Autoscaling_Group",
    MinSize=2, #minimum number of instances for this group
    MaxSize=3, #maximum number of instances for this group
    LaunchConfigurationName="jahnavi",
    AvailabilityZones=['us-east-1a'],
)
print(res)
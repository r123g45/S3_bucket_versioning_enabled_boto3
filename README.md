# S3_bucket_versioning_enabled_boto3

This process need to pass the profile name stored in ~/.aws/config file to link boto3 with the AWS session. to do so use the below commands.

# configure the sso 
   aws configure sso --- provide all the details 
# login to the profile for which you want to get the details
   aws sso login --profile <profile name>.   -------> accept the request from browser 
 
 edit the python script -- pass the profile name for which you want to get the details.
  
 This script will create two file with the name of profile name. one is txt file and other is excel file to your current directory.

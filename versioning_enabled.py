import boto3
import pandas as pd
account_name = '<profile_name>'
boto3.setup_default_session(profile_name=''+account_name+'')
total_bucket = 0
count = 0
s3client = boto3.client('s3')
f = open(''+account_name+'.txt', 'w')

for bucket in s3client.list_buckets()['Buckets']:
  total_bucket =total_bucket + 1
  bucket = bucket['Name']
  response = s3client.get_bucket_versioning(Bucket=bucket)
  if 'Status' in response and response['Status'] == 'Enabled':
    count = count + 1
    f.writelines(f'{bucket},YES\n')
  else:
    f.writelines(f'{bucket},NO \n')
f.close()

read_file = pd.read_csv(r''+account_name+'.txt')
read_file.to_csv(r''+account_name+'.csv', index=None)

print(f'Bucket enabled versioning : {str(count)}')
print(f'total bucket count: {str(total_bucket)}')

import boto3
client = boto3.client('iam')
response = client.list_open_id_connect_providers()
print(response)
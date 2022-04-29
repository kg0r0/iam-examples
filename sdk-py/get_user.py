import boto3
client = boto3.client('iam')
username = input("[*] Enter Your Username: ")
response = client.get_user(
  UserName=username
)
print(response)
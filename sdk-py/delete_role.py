import boto3
client = boto3.client('iam')
role_name = input("[*] Enter Role Name: ")
response = client.delete_role(
    RoleName=role_name
)
print(response)

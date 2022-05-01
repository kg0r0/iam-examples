import boto3
client = boto3.client('iam')
role_name = input("[*] Enter Role  Name: ")
policy = '''{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": { "AWS": "arn:aws:iam::123456789012:root" },
                    "Action": "sts:AssumeRole",
                    "Condition": { "Bool": { "aws:MultiFactorAuthPresent": "true" } }
                }
            ]
         }'''

response = client.update_assume_role_policy(
    RoleName=role_name,
    PolicyDocument=policy
)
print(response)

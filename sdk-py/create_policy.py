import boto3
client = boto3.client('iam')
policy_name = input("[*] Enter Policy Name: ")
bucket_name = input("[*] Enter Bucket Name: ")
policy = '''{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": [
                        "s3:ListAllMyBuckets"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:s3:::*"
                },
                {
                    "Action": "s3:*",
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:s3:::%s*",
                        "arn:aws:s3:::%s*/*"
                    ]
                }
            ]
         }''' % (bucket_name, bucket_name)

response = client.create_policy(
    PolicyName=policy_name,
    PolicyDocument=policy
)
print(response)

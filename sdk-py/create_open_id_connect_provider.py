import boto3
client = boto3.client('iam')
response = client.create_open_id_connect_provider(
    Url='https://token.actions.githubusercontent.com',
    ClientIDList=[
        'sts.amazonaws.com',
    ],
    ThumbprintList=[
        '3768084dfb3d2b68b7897bf5f565da8efEXAMPLE',
    ],
)
print(response)
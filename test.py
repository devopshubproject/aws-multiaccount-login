# import json

# AWS_ACCOUNTS_FILE = "aws_accounts.json"

# try:
#     with open(AWS_ACCOUNTS_FILE, "r") as f:
#         aws_accounts = json.load(f)
#     print("✅ JSON Loaded Successfully:", aws_accounts)
# except Exception as e:
#     print("❌ JSON Error:", e)


import boto3

role_arn = "arn:aws:iam::<aws-account-ids>:role/AWSConsoleAccessRole"

sts_client = boto3.client("sts")

try:
    assumed_role = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName="TestSession"
    )
    print("✅ STS Assume Role Success:", assumed_role["Credentials"])
except Exception as e:
    print("❌ Error Assuming Role:", e)

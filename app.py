import boto3
import json
from botocore.exceptions import ClientError

def get_secret(secret_name):
    client = boto3.client('secretsmanager')

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return response['SecretString']

    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        return None

if __name__ == "__main__":
    secret_name = "MyAppSecret"  # Replace with your actual secret name
    secret = get_secret(secret_name)

    if secret:
        print("Secret retrieved successfully ✅")
        # print(secret) or print(secret["key"]) if it's a JSON object
    else:
        print("Failed to retrieve secret ❌")

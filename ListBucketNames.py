import boto3
from botocore.exceptions import ClientError


def main():

    s3 = boto3.client('s3')

    response = s3.list_buckets()

    buckets = [bucket['Name'] for bucket in response['Buckets']]

    print(f"Bucket List {buckets}")


if __name__ == "__main__":
    main()

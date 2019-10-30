import logging
import boto3
from botocore.exceptions import ClientError


def copy_object(src_bucket_name, src_object_name, dest_bucket_name, dest_object_name):
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    
    if dest_object_name is None:
        dest_object_name = src_object_name

    s3 = boto3.client('s3')

    try:
        print("Before copying file to destination.")
        s3.copy_object(CopySource=copy_source,
                       Bucket=dest_bucket_name, Key=dest_object_name)
        print("Success copying file to destination.")

    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():

    src_bucket_name = 'botosourcedemo'
    src_object_name = 'test.txt'
    dest_bucket_name = 'botodestdemo'
    dest_object_name = 'test.txt'
    success = copy_object(src_bucket_name, src_object_name,
                          dest_bucket_name, dest_object_name)

    if success:
        logging.info(f'Copied {src_bucket_name}/{src_object_name} to '
                     f'{dest_bucket_name}/{dest_object_name}')


if __name__ == "__main__":
    main()

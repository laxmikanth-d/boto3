import boto3


def main():

    source_bucket = 'botosourcedemo'
    destination_bucket = 'botodestdemo'

    s3_client = boto3.client('s3')

    for key in s3_client.list_objects_v2(Bucket=source_bucket)['Contents']:
        file_name = key['Key']

        copy_source = {'Bucket': source_bucket, 'Key': file_name}
        s3_client.copy_object(Bucket=destination_bucket,
                              CopySource=copy_source, Key=file_name)
        print(f'{file_name} copied sucessfully')


if __name__ == "__main__":
    main()

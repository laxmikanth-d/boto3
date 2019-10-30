import boto3


def main():
    destination_bucket = 'botodestdemo'
    client = boto3.client('s3')

    # List items before deleting

    for item in client.list_objects_v2(Bucket=destination_bucket)['Contents']:
        item = item['Key']

        response = client.delete_objects(
            Bucket=destination_bucket,
            Delete={
                'Objects': [
                    {
                        'Key': item
                    },
                ],
                'Quiet': True
            }
        )

        print(response)

    # response = client.delete_bucket(Bucket=destination_bucket)
    print(response)

if __name__ == '__main__':
    main()

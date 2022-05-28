import boto3

s3 = boto3.client('s3')

# https://sandeepm-test1.s3.us-west-2.amazonaws.com/dummy.rtf
# s3://sandeepm-test1/dummy.rtf

# Cross account s3 bucket. Just provide the bucket name 
# as if like local account.

s3_bucket = 'input-files-json'
s3_bucket = 'sandeepm-test1'

res = s3.upload_file('test.txt', s3_bucket, Key='test2.txt')
print(res)

print('------------------------------------')

bkt = s3.list_objects(Bucket=s3_bucket)

for obj in bkt['Contents']:
    print(obj)

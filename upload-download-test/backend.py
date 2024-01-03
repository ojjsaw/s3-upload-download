import boto3
import time

EXPIRY_TIME=1800 # 30mins
ACCESS_KEY='AKIA4UQN57YSYG4VU3ND'
SECRET_KEY='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'
BUCKET_NAME='s3-upload-download-test2'
#s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
#presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': BUCKET_NAME, 'Key': object_key}, ExpiresIn=EXPIRY_TIME)

# read all file paths

# for each file path
# generate presigned upload url
# post file
# generate presigned download url
# download file

# count length of files
# gernerate n presigned upload urls
# post all files
# count length of files
# generate n presigned download urls
# download all files

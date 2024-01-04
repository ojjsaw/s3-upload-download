import boto3
import logging

class S3Utils:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token=None):
        self.bucket = bucket_name
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )

    def generate_presigned_upload_url(self, object_key, expiration=1800):
        try:
            presigned_url = self.s3.generate_presigned_url(
                'put_object',
                Params={'Bucket': self.bucket, 'Key': object_key},
                ExpiresIn=expiration
            )
            return presigned_url
        except Exception as ex:
            logging.error(str(ex))
            return None

    def generate_presigned_download_url(self, object_key, expiration=1800):
        try:
            presigned_url = self.s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket, 'Key': object_key},
                ExpiresIn=expiration
            )
            return presigned_url
        except Exception as ex:
            logging.error(str(ex))
            return None

    def generate_presigned_list_url(self, prefix, expiration=1800):
        try:
            presigned_url = self.s3.generate_presigned_url(
                'list_objects_v2',
                Params={'Bucket': self.bucket, 'Prefix': prefix},
                ExpiresIn=expiration
            )
            return presigned_url
        except Exception as ex:
            logging.error(str(ex))
            return None
        
    def delete_all_data_s3(self, prefix):
        objects_to_delete = []
        paginator = self.s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=self.bucket, Prefix=prefix):
            for obj in page.get('Contents', []):
                objects_to_delete.append({'Key': obj['Key']})
        
        if objects_to_delete:
            self.s3.delete_objects(Bucket=self.bucket, Delete={'Objects': objects_to_delete})
        else:
            print(f"No objects found under {prefix} in bucket {self.bucket}")
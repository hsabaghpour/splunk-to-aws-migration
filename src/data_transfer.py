import boto3
import logging

class DataTransfer:
    def __init__(self, bucket_name, region="us-east-1"):
        self.s3_client = boto3.client("s3", region_name=region)
        self.bucket_name = bucket_name

    def upload_to_s3(self, file_path, key):
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, key, ExtraArgs={"ServerSideEncryption": "aws:kms"})
            logging.info(f"File {file_path} uploaded to {self.bucket_name}/{key}")
        except Exception as e:
            logging.error(f"Error during data transfer: {e}")

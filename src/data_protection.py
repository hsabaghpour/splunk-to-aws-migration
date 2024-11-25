import boto3
import logging

class DataProtection:
    def __init__(self, macie_client=None):
        self.macie_client = macie_client or boto3.client("macie2")

    def run_dlp_scan(self, bucket_name):
        try:
            response = self.macie_client.create_classification_job(
                jobType="ONE_TIME",
                s3JobDefinition={
                    "bucketDefinitions": [{"accountId": "your-account-id", "buckets": [bucket_name]}]
                },
            )
            logging.info(f"DLP Scan initiated: {response['jobId']}")
        except Exception as e:
            logging.error(f"Error during DLP scan: {e}")

import unittest
from src.data_transfer import DataTransfer
from unittest.mock import patch

class TestDataTransfer(unittest.TestCase):
    @patch("src.data_transfer.boto3.client")
    def test_upload_to_s3_success(self, mock_client):
        mock_s3 = mock_client.return_value
        transfer = DataTransfer("test-bucket")
        transfer.upload_to_s3("test-file.txt", "test-key")
        mock_s3.upload_file.assert_called_once_with(
            "test-file.txt",
            "test-bucket",
            "test-key",
            ExtraArgs={"ServerSideEncryption": "aws:kms"}
        )

if __name__ == "__main__":
    unittest.main()

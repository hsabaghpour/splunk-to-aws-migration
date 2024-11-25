import unittest
from src.data_protection import DataProtection
from unittest.mock import patch

class TestDataProtection(unittest.TestCase):
    @patch("src.data_protection.boto3.client")
    def test_run_dlp_scan(self, mock_client):
        mock_macie = mock_client.return_value
        protection = DataProtection(mock_macie)
        protection.run_dlp_scan("test-bucket")
        mock_macie.create_classification_job.assert_called_once()

if __name__ == "__main__":
    unittest.main()

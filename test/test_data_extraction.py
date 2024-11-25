import unittest
from src.data_extraction import DataExtractor
from unittest.mock import patch

class TestDataExtractor(unittest.TestCase):
    @patch("src.data_extraction.requests.get")
    def test_extract_logs_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [{"log": "test log"}]}

        extractor = DataExtractor("https://splunk-instance", "test-token")
        logs = extractor.extract_logs("search test query")
        self.assertEqual(logs, [{"log": "test log"}])

    @patch("src.data_extraction.requests.get")
    def test_extract_logs_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        extractor = DataExtractor("https://splunk-instance", "test-token")
        logs = extractor.extract_logs("search test query")
        self.assertIsNone(logs)

if __name__ == "__main__":
    unittest.main()

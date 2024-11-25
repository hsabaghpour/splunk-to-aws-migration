import unittest
from src.data_analysis import DataAnalysis
from unittest.mock import patch

class TestDataAnalysis(unittest.TestCase):
    @patch("src.data_analysis.boto3.client")
    def test_execute_query(self, mock_client):
        mock_athena = mock_client.return_value
        analysis = DataAnalysis()
        analysis.execute_query("SELECT * FROM test_table", "test_db", "s3://test-output")
        mock_athena.start_query_execution.assert_called_once()

if __name__ == "__main__":
    unittest.main()

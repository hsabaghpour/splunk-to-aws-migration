import requests
import logging

class DataExtractor:
    def __init__(self, splunk_url, splunk_token):
        self.splunk_url = splunk_url
        self.headers = {"Authorization": f"Bearer {splunk_token}"}

    def extract_logs(self, query):
        try:
            response = requests.get(f"{self.splunk_url}/search", headers=self.headers, params={"query": query})
            response.raise_for_status()
            return response.json()["results"]
        except Exception as e:
            logging.error(f"Error during data extraction: {e}")
            return None

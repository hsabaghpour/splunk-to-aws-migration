import boto3
import logging

class DataAnalysis:
    def __init__(self):
        self.athena_client = boto3.client("athena")

    def execute_query(self, query, database, output_location):
        try:
            response = self.athena_client.start_query_execution(
                QueryString=query,
                QueryExecutionContext={"Database": database},
                ResultConfiguration={"OutputLocation": output_location},
            )
            logging.info(f"Query started: {response['QueryExecutionId']}")
        except Exception as e:
            logging.error(f"Error during data analysis: {e}")

from src.data_extraction import DataExtractor
from src.data_transfer import DataTransfer
from src.data_validation import DataValidator
from src.data_protection import DataProtection
from src.data_analysis import DataAnalysis

def main():
    # Configurations
    splunk_url = "https://splunk-instance"
    splunk_token = "your-splunk-token"
    query = "search index=network_logs | stats count by KPI"
    bucket_name = "your-s3-bucket"
    file_path = "network_logs.json"
    key = "logs/network_logs.json"
    athena_database = "network_data"
    athena_output = "s3://your-athena-output-bucket/"

    # Step 1: Extract Data
    extractor = DataExtractor(splunk_url, splunk_token)
    logs = extractor.extract_logs(query)
    with open(file_path, "w") as f:
        f.write(str(logs))

    # Step 2: Transfer to AWS
    transfer = DataTransfer(bucket_name)
    transfer.upload_to_s3(file_path, key)

    # Step 3: Validate Data
    validator = DataValidator()
    source_checksum = validator.calculate_checksum(file_path)
    # Assuming checksum from AWS S3 is fetched separately
    validator.validate_checksum(source_checksum, "expected_checksum_from_s3")

    # Step 4: Run DLP
    protection = DataProtection()
    protection.run_dlp_scan(bucket_name)

    # Step 5: Analyze Data
    analysis = DataAnalysis()
    analysis.execute_query("SELECT * FROM network_logs LIMIT 10;", athena_database, athena_output)

if __name__ == "__main__":
    main()
# this is to test git push
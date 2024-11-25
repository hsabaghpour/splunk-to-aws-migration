import logging

def setup_logging(log_file="migration.log"):
    """Configures logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def read_json(file_path):
    """Reads a JSON file and returns its contents."""
    import json
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
        return None

def write_json(data, file_path):
    """Writes data to a JSON file."""
    import json
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data written to {file_path}")
    except Exception as e:
        logging.error(f"Error writing to JSON file {file_path}: {e}")

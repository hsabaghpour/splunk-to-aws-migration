import hashlib
import logging

class DataValidator:
    @staticmethod
    def calculate_checksum(file_path):
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()

    @staticmethod
    def validate_checksum(source_checksum, target_checksum):
        if source_checksum == target_checksum:
            logging.info("Checksum validation passed.")
            return True
        else:
            logging.error("Checksum validation failed.")
            return False

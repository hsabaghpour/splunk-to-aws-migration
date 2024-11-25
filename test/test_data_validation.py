import unittest
from src.data_validation import DataValidator

class TestDataValidator(unittest.TestCase):
    def test_calculate_checksum(self):
        with open("test_file.txt", "w") as f:
            f.write("test content")
        checksum = DataValidator.calculate_checksum("test_file.txt")
        self.assertEqual(len(checksum), 64)

    def test_validate_checksum(self):
        self.assertTrue(DataValidator.validate_checksum("abc123", "abc123"))
        self.assertFalse(DataValidator.validate_checksum("abc123", "def456"))

if __name__ == "__main__":
    unittest.main()

# to update the github repository with the latest changes, run the following commands:
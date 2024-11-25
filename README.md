# splunk-to-aws-migration

# Splunk to AWS Migration with Data Protection and DLP

## Overview

This project demonstrates how to migrate logs and KPIs from Splunk to AWS using Python, ensuring data protection, encryption, and Data Loss Prevention (DLP) compliance.

## Features

- **Data Extraction:** Retrieves logs from Splunk via APIs.
- **Data Transfer:** Transfers data securely to AWS S3 with KMS encryption.
- **Data Validation:** Validates data integrity using checksum mechanisms.
- **Data Protection:** Implements AWS Macie for DLP scans.
- **Data Analysis:** Analyzes KPIs using AWS Athena.

## Prerequisites

- Python 3.8+
- AWS account with S3, Macie, and Athena enabled
- Splunk API access

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hsabaghpour/splunk-to-aws-migration.git
   cd splunk-to-aws-migration
   ```

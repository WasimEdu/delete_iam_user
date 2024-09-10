# IAM User Management Script

**Author:** Wasim

This Python script helps to manage IAM users by detaching policies, deleting the login profile, and ultimately deleting the user from AWS IAM. 

## Overview

The script performs the following actions:

1. Detaches specified IAM policies from a given user.
2. Deletes the login profile of the specified user.
3. Deletes the IAM user.

## Prerequisites

- **AWS Account**: You need an AWS account to run this script.
- **AWS CLI Configured**: Ensure you have the AWS CLI configured with a profile named `default` or modify the script to use your specific profile.
- **Boto3 Library**: This script uses the Boto3 library, which must be installed. You can install it via pip if you haven't already.

## Usage

1. **Setup AWS Credentials**:
   Ensure that your AWS credentials are set up. You can configure them using the AWS CLI:
   ```sh
   aws configure

2. **Require module**:
   Install boto3 module:
   ```sh
   pip install boto3

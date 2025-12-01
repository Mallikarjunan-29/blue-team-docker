import boto3
import gzip
import json
import os
from datetime import datetime
from io import BytesIO

# === CONFIGURATION ===
BUCKET_NAME = 'aws-cloudtrail-logs-002125562743-9dd280fb' #use your s3 bucket name
ACCOUNT_ID = '002125562743' # Use your account id
REGIONS = ['us-east-1', 'us-east-2']
DEST_FOLDER = os.path.expanduser('~/blue-team-docker/splunk/splunk_logs/aws')  # Relative path from scripts folder- maintain the folder structure or give the correct path under home/<user>/

# Create S3 client
s3 = boto3.client('s3')

def download_and_extract_logs(region):
    prefix = f"AWSLogs/{ACCOUNT_ID}/CloudTrail/{region}/"
    print(f"\n📡 Checking region: {region}")

    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)

    if 'Contents' not in response:
        print(f"❌ No logs found in region {region}")
        return

    for obj in response['Contents']:
        key = obj['Key']
        if key.endswith(".json.gz"):
            file_name = key.split('/')[-1].replace('.json.gz', f'.json')
            dest_path = os.path.join(DEST_FOLDER, file_name)

            if os.path.exists(dest_path):
                continue  # Skip already downloaded

            print(f"⬇️  Downloading: {key}")

            # Download and decompress
            gzipped_obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
            with gzip.GzipFile(fileobj=BytesIO(gzipped_obj['Body'].read())) as gzipfile:
                data = gzipfile.read()

                # Write uncompressed log to destination
                with open(dest_path, 'wb') as f:
                    f.write(data)
                    print(f"✅ Saved to: {dest_path}")

if __name__ == "__main__":
    os.makedirs(DEST_FOLDER, exist_ok=True)
    for region in REGIONS:
        download_and_extract_logs(region)

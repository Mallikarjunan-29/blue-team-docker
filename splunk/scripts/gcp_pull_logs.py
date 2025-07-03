import os
from google.cloud import storage
from datetime import datetime

# --- Config ---
BUCKET_NAME = "my-gcp-audit-logs-arjun2407"
DEST_DIR = "~/blue-team-docker/splunk/splunk_logs/gcplogs"
PREFIX = "cloudaudit.googleapis.com/activity/"

# --- Auth via gcloud CLI ---
# Assumes you've already authenticated using `gcloud auth application-default login`
storage_client = storage.Client()

def download_new_logs():
    bucket = storage_client.bucket(BUCKET_NAME)
    blobs = bucket.list_blobs(prefix=PREFIX)

    os.makedirs(DEST_DIR, exist_ok=True)

    for blob in blobs:
        # Skip folders
        if blob.name.endswith("/"):
            continue

        dest_path = os.path.join(DEST_DIR, blob.name.replace("/", "_"))

        if not os.path.exists(dest_path):
            print(f"Downloading {blob.name} → {dest_path}")
            blob.download_to_filename(dest_path)

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting log pull...")
    download_new_logs()
    print(f"[{datetime.now()}] Done.")

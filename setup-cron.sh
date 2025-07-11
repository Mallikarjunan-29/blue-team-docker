#!/bin/bash
# setup-cron.sh – Install cron job for GCP log pull script
# Get absolute path to THIS script

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "Installing GCP Cron"

# Python script (relative to repo structure)
GCP_SCRIPT_PATH="$BASE_DIR/splunk/scripts/gcp_pull_logs.py"

# Log output (goes into Cronlog folder at repo root)
GCP_LOG_FILE="$BASE_DIR/Cronlog/gcppull.log"

# Cron command (every 5 minutes)
CRON_CMD="*/5 * * * * /usr/bin/python3 $GCP_SCRIPT_PATH >> $GCP_LOG_FILE 2>&1"

# Install cron if not already set
( crontab -l 2>/dev/null | grep -Fv "$GCP_SCRIPT_PATH" ; echo "$CRON_CMD" ) | crontab -

echo "✅ Cron job installed or already exists:"
echo "$CRON_CMD"


echo "Installing S3 Cron"

# Python script (relative to repo structure)
S3_SCRIPT_PATH="$BASE_DIR/splunk/scripts/s3_pull_logs.py"

# Log output (goes into Cronlog folder at repo root)
S3_LOG_FILE="$BASE_DIR/Cronlog/S3pull.log"

# Cron command (every 5 minutes)
CRON_CMD="*/5 * * * * /usr/bin/python3 $S3_SCRIPT_PATH >> $S3_LOG_FILE 2>&1"

# Install cron if not already set
( crontab -l 2>/dev/null | grep -Fv "$S3_SCRIPT_PATH" ; echo "$CRON_CMD" ) | crontab -

echo "✅ Cron job installed or already exists:"
echo "$CRON_CMD"


echo "Installing GUARDDUTY Cron"

# Python script (relative to repo structure)
GD_SCRIPT_PATH="$BASE_DIR/splunk/scripts/boto_guardduty_pull_logs.py"

# Log output (goes into Cronlog folder at repo root)
GD_LOG_FILE="$BASE_DIR/Cronlog/GDpull.log"

# Cron command (every 5 minutes)
CRON_CMD="*/5 * * * * /usr/bin/python3 $GD_SCRIPT_PATH >> $GD_LOG_FILE 2>&1"

# Install cron if not already set
( crontab -l 2>/dev/null | grep -Fv "$GD_SCRIPT_PATH" ; echo "$CRON_CMD" ) | crontab -

echo "✅ Cron job installed or already exists:"
echo "$CRON_CMD"

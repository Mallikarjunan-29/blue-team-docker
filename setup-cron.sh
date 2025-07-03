#!/bin/bash
# setup-cron.sh – Install cron job for GCP log pull script
# Get absolute path to THIS script
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

# Python script (relative to repo structure)
SCRIPT_PATH="$BASE_DIR/splunk/scripts/gcp_pull_logs.py"

# Log output (goes into Cronlog folder at repo root)
LOG_FILE="$BASE_DIR/Cronlog/gcppull.log"

# Cron command (every 5 minutes)
CRON_CMD="*/5 * * * * /usr/bin/python3 $SCRIPT_PATH >> $LOG_FILE 2>&1"

# Install cron if not already set
( crontab -l 2>/dev/null | grep -Fv "$SCRIPT_PATH" ; echo "$CRON_CMD" ) | crontab -

echo "✅ Cron job installed or already exists:"
echo "$CRON_CMD"

#!/bin/bash
# setup-cron.sh – Install cron job for GCP log pull script

# Use full path for script location
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/gcp_pull_logs.py"
LOG_DIR="$(cd "$(dirname "$0")" && pwd)/Cronlog"
LOG_FILE="$LOG_DIR/gcppull.log"

# Cron command (every 5 minutes)
CRON_CMD="*/5 * * * * /usr/bin/python3 $SCRIPT_PATH >> $LOG_FILE 2>&1"

# Install cron if not already set
( crontab -l 2>/dev/null | grep -Fv "$SCRIPT_PATH" ; echo "$CRON_CMD" ) | crontab -

echo "✅ Cron job installed or already exists:"
echo "$CRON_CMD"

#!/bin/bash

# Script: Class 01 challenge syslog_backup.sh
# Description:
# Copies /var/log/syslog to the current working directory, appends the current date and time to the filename,
#              and includes timestamped echo statements.

# Timestamp function
timestamp() {
  echo "[$(date '+%Y-%m-%d')]"
}

# Echo statement with timestamp
echo "$(timestamp) Starting syslog backup..."

# Source and destination file paths
source_file="/var/log/syslog"
destination_file="syslog_backup_$(date '+%Y%m%d').log"

# Echo statement with timestamp
echo "$(timestamp) Copying syslog to $destination_file..."

# Copy syslog to the current working directory
cp "$source_file" "$destination_file"

# Check if the copy was successful
if [ $? -eq 0 ]; then
  echo "$(timestamp) Copy successful!"
else
  echo "$(timestamp) Copy failed. Please check permissions or try again."
  exit 1
fi

# Echo statement with timestamp
echo "$(timestamp) Backup complete. The file is stored as: $destination_file"

# This scrips was created with help from ChatGTP3.5
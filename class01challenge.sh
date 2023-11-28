#!/bin/bash

# Script: Class 01 challenge syslog_backup.sh
# Date 11/28/2023 
# Will Baur 
# Description:
# Copies /var/log/syslog to the current working directory, appends the current date and time to the filename,
#              and includes timestamped echo statements.

# Timestamp function
timestamp() {
  echo "[$(date '+%Y-%m-%d')]"
}

# Echo statement with timestamp letting user know process has begun
echo "$(timestamp) Starting syslog backup..."

# The File Source and destination file path where we are storing the file
source_file="/var/log/syslog"
destination_file="syslog_backup_$(date '+%Y%m%d').log"

# Echo statement with timestamp
echo "$(timestamp) Copying syslog to $destination_file..."

# Copy syslog to the current directory
cp "$source_file" "$destination_file"

# Perform a check to see if the copy was successful
if [ $? -eq 0 ]; then
  echo "$(timestamp) Copy successful!"
else
  echo "$(timestamp) Copy failed. Please check permissions or try again."
  exit 1
fi

# Let the user know where the new file is stored and its name
echo "$(timestamp) Backup complete. The file is stored as: $destination_file"

# This scrips was created with help from ChatGTP3.5
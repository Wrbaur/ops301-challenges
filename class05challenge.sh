#!/bin/bash

# Ops 301 challenge 5
# Authur: Will B. with the help of ChatGPT
# 12/01/2023


# Purpose Write a bash script that performs the following tasks:
# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS


# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script with sudo or as root."
    exit 1
fi


# Print original file sizes
echo "Original File Sizes:"
echo "syslog: $(du -h /var/log/syslog | cut -f1)"
echo "wtmp: $(du -h /var/log/wtmp | cut -f1)"

# Compress and backup log files
backup_dir="/var/log/backups"
timestamp=$(date "+%Y%m%d%H%M%S")
mkdir -p "$backup_dir"
zip_file_syslog="$backup_dir/syslog-$timestamp.zip"
zip_file_wtmp="$backup_dir/wtmp-$timestamp.zip"

gzip -c /var/log/syslog > "$zip_file_syslog"
gzip -c /var/log/wtmp > "$zip_file_wtmp"

# Clear log files
echo "Clearing log files..."
truncate -s 0 /var/log/syslog
truncate -s 0 /var/log/wtmp

# Print compressed file sizes
echo -e "\nCompressed File Sizes:"
echo "syslog: $(du -h "$zip_file_syslog" | cut -f1)"
echo "wtmp: $(du -h "$zip_file_wtmp" | cut -f1)"

# Compare file sizes
echo -e "\nComparison:"
echo "syslog size difference: $(du -h /var/log/syslog | cut -f1) -> $(du -h "$zip_file_syslog" | cut -f1)"
echo "wtmp size difference: $(du -h /var/log/wtmp | cut -f1) -> $(du -h "$zip_file_wtmp" | cut -f1)"
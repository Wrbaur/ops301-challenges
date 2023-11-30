#!/bin/bash

# Ops 301 challenge 3
# Authur: Will B. with the help of ChatGPT
# 11/29/2023

# Purpose create a bash script that alters file permissions of everything in a directory.

# Ask's the user for the directory path 
echo "Enter the directory path:"
read directory

# Check to see if the directory exisits 
if [ ! -d "$directory" ]; then
    echo "Error: The directory doesnt exist."
    exit 1
fi

# Ask the user for the permissions
echo "Enter the permissions"
read permissions

# Change permissions for all the files in the specified directory 
chmod -R "$permissions" "$directory"

echo -e "\nNew Permissions settings:"
ls -l "$directory" | `awk `{print $1, $9}`


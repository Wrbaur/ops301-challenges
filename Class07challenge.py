#!/usr/bin/env python3
# Script: Ops 301 challenge 7
# Authur: Will B. with the help of ChatGPT
# Date: 12/05/2023
 
# Purpose Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Import libraries
import os

# Declaration of functions
def directory_structure(user_path):
    directory_structure = []

    for (root, dirs, files) in os.walk(user_path):
        # Add current directory to the tuple
        current_directory = (root, dirs, files)
        directory_structure.append(current_directory)

    return directory_structure

# Main
# Read user input into a variable
user_input_path = input("Enter the directory path: ")

# Call the function to generate directory structure
result = directory_structure(user_input_path)

# Print the generated directory structure
for entry in result:
    print(f"Current Directory: {entry[0]}")
    
    # Print subdirectories
    print("Subdirectories:")
    for dir_name in entry[1]:
        print(os.path.join(entry[0], dir_name))

    # Print files
    print("Files:")
    for file_name in entry[2]:
        print(os.path.join(entry[0], file_name))
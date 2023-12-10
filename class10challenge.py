#!/usr/bin/env python3
# Script: Ops 301 challenge 10
# Authur: Will B. with the help of ChatGPT
# Date: 12/10/2023
 
# Objectives Using file handling commands, create a Python script that creates a new .txt file,
# appends three lines, prints to the screen the first line, then deletes the .txt file.

# Import Libraries 
import os

# Creating a new .txt file
with open('example.txt', 'w') as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Reading and printing the first line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First Line:", first_line)

    file_path = 'example.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")
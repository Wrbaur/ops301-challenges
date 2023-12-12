#!/usr/bin/env python3
# Script: Ops 301 challenge 12
# Authur: Will B. with the help of ChatGPT
# Date: 12/12/2023
 
# Objectives Create a Python script that performs the following: Prompt the user to type a string input as the variable for your destination URL.
# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.

# Import Libraries 
import requests
import re

# Function to validate and correct the URL format
def validate_and_correct_url(user_input):
    # Check if the input starts with 'http://' or 'https://'
    if not re.match(r'https?://', user_input):
        # If not, add 'https://' to the beginning
        user_input = 'https://' + user_input
    return user_input

# Prompt the user to enter a destination URL
url = input("Enter the destination URL: ")

# Validate and correct the URL format
url = validate_and_correct_url(url)

# Prompt the user to select an HTTP method
valid_http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
http_method = ''

while http_method not in valid_http_methods:
    http_method = input("Select a valid HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the entire request information
print(f"\nRequest about to be sent:\nURL: {url}\nHTTP Method: {http_method}")

# Ask the user to confirm before proceeding
confirmation = input("Do you want to proceed? (yes/y or no/n): ").lower()

if confirmation in ['yes', 'y']:
    # Perform the request using the requests library
    response = requests.request(http_method, url)

    # Translate status code into plain terms
    status_code_translation = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        500: 'Internal Server Error',
        # Add more status codes with corresponding messages
    }

    # Print translated status message
    translated_status = status_code_translation.get(response.status_code, 'Unknown Status Code')
    print(f"\nStatus Code: {response.status_code} - {translated_status}")

    # Print response header information
    print("\nResponse Header Information:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
else:
    print("Request canceled.")
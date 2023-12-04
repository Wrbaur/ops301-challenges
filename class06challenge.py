# Ops 301 challenge 6
# Authur: Will B. with the help of ChatGPT
# 12/04/2023


# Purpose In Ubuntu, create a Python script that executes a few bash commands successfully. 
# Indicate in comments how you achieved this.


# Import the OS mondual 

import os

# Declare variables
name = "John"
age = 25
location = "Ubuntu"

# Print variable values
print("Name:", name)
print("Age:", age)
print("Location:", location)

# Execute bash commands using os.system
print("\nExecuting Bash Commands:")
os.system("whoami")
os.system("ip a")
os.system("lshw -short")
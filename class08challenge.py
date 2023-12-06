#!/usr/bin/env python3
# Script: Ops 301 challenge 8
# Authur: Will B. with the help of ChatGPT
# Date: 12/06/2023
 
# Purpose Create a Python script that includes the following:
# Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.

#Import Libraries 
import os
from colorama import init, Fore  # Import colorama and necessary components
from termcolor import colored

# Initialize colorama
init(autoreset=True)

# Colored header
print(f"{Fore.BLUE}Class08challenge{Fore.RESET}\n")

# list of ten elements
my_list = ["cereal", "soda", "cherry", "apple", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Print fourth element
print(colored("Fourth element:", "yellow"), my_list[3], "\n")

# Print sixth through tenth element
print(colored("Sixth through tenth elements:", "red"), my_list[5:10], "\n")

# Change the value of the seventh element to “onion”
my_list[6] = "onion"

# Stretch Goals
# Use Python methods to manipulate the list
my_list.append("mango")  # Add "mango" to the end of the list
print(colored("List after append:", "yellow"), my_list, "\n")

my_list_copy = my_list.copy()  # Create a copy of the list
print(colored("Copy of the list:", "red"), my_list_copy, "\n")

date_count = my_list.count("date")  # Count occurrences of "date" in the list
print(colored("Count of 'date':", "yellow"), date_count, "\n")

additional_elements = ["nectarine", "orange"]
my_list.extend(additional_elements)  # Extend the list with additional elements
print(colored("List after extend:", "red"), my_list, "\n")

kiwi_index = my_list.index("kiwi")  # Find the index of "kiwi" in the list
print(colored("Index of 'kiwi':", "yellow"), kiwi_index, "\n")

my_list.insert(2, "blueberry")  # Insert "blueberry" at index 2
print(colored("List after insert:", "red"), my_list, "\n")

removed_element = my_list.pop()  # Remove and return the last element
print(colored("Removed element:", "yellow"), removed_element, "\n")
print(colored("List after pop:", "red"), my_list, "\n")

my_list.remove("soda")  # Remove the first occurrence of "banana"
print(colored("List after remove:", "yellow"), my_list, "\n")

my_list.reverse()  # Reverse the order of elements in the list
print(colored("List after reverse:", "red"), my_list, "\n")

sorted_list = sorted(my_list)
print(colored("List after sort:", "yellow"), sorted_list, "\n")

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Create a set
my_set = {1, 2, 3, 4, 5}

# Create a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
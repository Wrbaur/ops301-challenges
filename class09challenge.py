#!/usr/bin/env python3
# Script: Ops 301 challenge 9
# Authur: Will B. with the help of ChatGPT
# Date: 12/07/2023
 
# ObjectivesCreate if statements using these logical conditionals below. 
# Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

#Import Libraries 

# Example variables
NFL = 5
NHL = 10

# Equals: NFL == NHL
if NFL == NHL:
    print("NFL is equal to NHL")
else:
    print("NFL is not equal to NHL")

# Not Equals: NFL != NHL
if NFL != NHL:
    print("NFL is not equal to NHL")
else:
    print("NFL is equal to NHL")

# Less than: NFL < NHL
if NFL < NHL:
    print("NFL is less than NHL")
else:
    print("NFL is not less than NHL")

# Less than or equal to: NFL <= NHL
if NFL <= NHL:
    print("NFL is less than or equal to NHL")
else:
    print("NFL is greater than NHL")

# Greater than: NFL > NHL
if NFL > NHL:
    print("NFL is greater than NHL")
else:
    print("NFL is not greater than NHL")

# Greater than or equal to: NFL >= NHL
if NFL >= NHL:
    print("NFL is greater than or equal to NHL")
else:
    print("NFL is less than NHL")

# Using if, elif, and else
MLB = 7

if MLB < NFL:
    print("MLB is less than NFL")
elif MLB == NFL:
    print("MLB is equal to NFL")
else:
    print("MLB is greater than NFL")

# Using if, elif, and else with multiple conditions
NBA = 15

if NBA < NFL:
    print("NBA is less than NFL")
elif NBA == NFL:
    print("NBA is equal to NFL")
elif NBA > NFL and NBA < NHL:
    print("NBA is between NFL and NHL")
else:
    print("NBA is greater than or equal to NHL")
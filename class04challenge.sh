#!/bin/bash

# Ops 301 challenge f
# Authur: Will B. with the help of ChatGPT
# 11/30/2023


# Purpose Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit

while true; do
    # Display the menu
    echo "Menu Options:"
    echo "1. Hello world (prints 'Hello world!' to the screen)"
    echo "2. Ping self (pings this computer's loopback address)"
    echo "3. IP info (print the network adapter information for this computer)"
    echo "4. Exit"

    # Get user input
    read -p "Enter your choice (1-4): " choice

    # Process user choice
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping self (loopback address) 4 times
            ;;
        3)
            ip addr show  # Display network adapter information
            ;;
        4)
            echo "Exiting the menu. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Add any additional logic or actions here
done
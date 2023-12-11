#!/usr/bin/env python3
# Script: Ops 301 challenge 11
# Authur: Will B. with the help of ChatGPT
# Date: 12/11/2023
 
# Objectives Create a Python script that fetches this information using Psutil:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

#Import Libraries 
import psutil

# Fetch system information using psutil

# Define the CPU times categories
categories = [
    "user",     # Time spent by normal processes executing in user mode
    "system",   # Time spent by processes executing in kernel mode
    "idle",     # Time when the system was idle
    "nice",     # Time spent by priority processes executing in user mode
    "iowait",   # Time spent waiting for I/O to complete
    "irq",      # Time spent for servicing hardware interrupts
    "softirq",  # Time spent for servicing software interrupts
    "steal",    # Time spent by other operating systems running in a virtualized environment
    "guest"     # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
]

# Fetch and print system information
for category in categories:
    time_value = getattr(psutil.cpu_times(), category)
    print(f"Time spent {'' if category in ['user', 'system', 'nice'] else 'for '} {category}: {time_value} seconds")



# Below is the code broken out but commented out

# # Time spent by normal processes executing in user mode
# user_time = psutil.cpu_times().user
# print(f"Time spent by normal processes executing in user mode: {user_time} seconds")

# # Time spent by processes executing in kernel mode
# system_time = psutil.cpu_times().system
# print(f"Time spent by processes executing in kernel mode: {system_time} seconds")

# # Time when the system was idle
# idle_time = psutil.cpu_times().idle
# print(f"Time when the system was idle: {idle_time} seconds")

# # Time spent by priority processes executing in user mode
# priority_user_time = psutil.cpu_times().nice
# print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")

# # Time spent waiting for I/O to complete
# io_wait_time = psutil.cpu_times().iowait
# print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")

# # Time spent for servicing hardware interrupts
# irq_time = psutil.cpu_times().irq
# print(f"Time spent for servicing hardware interrupts: {irq_time} seconds")

# # Time spent for servicing software interrupts
# soft_irq_time = psutil.cpu_times().softirq
# print(f"Time spent for servicing software interrupts: {soft_irq_time} seconds")

# # Time spent by other operating systems running in a virtualized environment
# steal_time = psutil.cpu_times().steal
# print(f"Time spent by other operating systems running in a virtualized environment: {steal_time} seconds")

# # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
# guest_time = psutil.cpu_times().guest
# print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {guest_time} seconds")
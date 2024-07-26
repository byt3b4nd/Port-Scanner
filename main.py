#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style

# Initialize colorama
init()

# Clear the screen
subprocess.call('clear', shell=True)

# Function to check if the host is up by trying to connect to a common port
def is_host_up(host, port=80, timeout=2):
    try:
        sock = socket.create_connection((host, port), timeout)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

# Ask for input
remoteServer = input(Fore.CYAN + "Enter a remote host to scan: " + Style.RESET_ALL)
try:
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.gaierror:
    print(Fore.RED + "Hostname could not be resolved. Exiting." + Style.RESET_ALL)
    sys.exit()

# Check if the host is up
if not is_host_up(remoteServerIP):
    print(Fore.RED + "Host is down or not reachable. Exiting." + Style.RESET_ALL)
    sys.exit()

# Print a nice banner with information on which host we are about to scan
print(Fore.YELLOW + "_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60 + Style.RESET_ALL)

# Check what time the scan started
t1 = datetime.now()

# Function to scan a single port
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout to 1 second to speed up closed port checks
    result = sock.connect_ex((remoteServerIP, port))
    sock.close()
    return port, result == 0

# Using ThreadPoolExecutor to scan ports concurrently
open_ports = []
with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(scan_port, port) for port in range(1, 1025)]
    for future in as_completed(futures):
        port, is_open = future.result()
        if is_open:
            print(Fore.GREEN + "Port {}: Open".format(port) + Style.RESET_ALL)

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print(Fore.CYAN + 'Scan Completed in: ', total, Style.RESET_ALL)

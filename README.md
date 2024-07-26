# Enhanced Port Scanner

This Python script performs a port scan on a specified remote host. It first checks if the host is reachable by attempting to connect to a common port (port 80). If the host is up, it proceeds to scan ports 1 through 1024 concurrently, displaying open ports with colored output for easy identification.

## Features

- Checks if the host is up before scanning.
- Concurrent scanning of ports for faster results.
- Colorful terminal output for better readability.
- Handles common errors gracefully.

## Prerequisites

- Python 3.x
- `colorama` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enhanced-port-scanner.git
   cd enhanced-port-scanner



## Usage
      cd enhanced-port-scanner
      pip install colorama 
      python enhanced_port_scanner.py



## Example
      Enter a remote host to scan: example.com
      Please wait, scanning remote host 93.184.216.34
      Port 80: Open
      Port 443: Open
      Scan Completed in:  0:00:05.123456


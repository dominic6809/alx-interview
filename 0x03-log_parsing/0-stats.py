#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
- After every 10 lines and/or a keyboard interruption (CTRL + C),
    print statistics from the beginning:
    * Total file size: File size: <total size>
    * Number of lines by status code in ascending order
"""
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the computed statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Regular expression pattern for log line validation
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

try:
    for line in sys.stdin:
        try:
            # Remove trailing whitespace
            line = line.strip()
            
            # Match the line against the pattern
            match = re.match(pattern, line)
            if match:
                # Extract status code and file size
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                
                # Update metrics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()
            
        except (ValueError, IndexError):
            # Skip lines that don't match the expected format
            continue
            
except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()
    sys.exit(0)

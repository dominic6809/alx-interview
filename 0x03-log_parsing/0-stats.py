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


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the total file size and counts of each status code in ascending order."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Check if the line has the correct format
        if len(parts) >= 7 and parts[5] == '"GET' and parts[6] == '/projects/260':
            # Extract and add file size if it's a valid integer
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except ValueError:
                continue
            
            # Extract and count the status code if it's valid
            try:
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                continue
            
        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when interrupted by Ctrl+C
    print_stats()
    raise

# Print final stats if end of file is reached
print_stats()

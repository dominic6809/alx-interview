#!/usr/bin/python3

import sys
import signal
import re

# Initialize metrics
total_file_size = 0
status_counts = {
    str(code): 0 for code in [
        200, 301, 400, 401, 403, 404, 405, 500
    ]
}
line_count = 0


def print_stats():
    """Print the current statistics: total file size and status code counts."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """Handle CTRL + C signal and print the stats before exiting."""
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Define regex pattern for log line validation
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

# Process each line from stdin
for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)

    # Only process lines that match the expected format
    if match:
        status_code, file_size = match.groups()
        file_size = int(file_size)

        # Update total file size
        total_file_size += file_size

        # Update status code count if it’s one of the tracked codes
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

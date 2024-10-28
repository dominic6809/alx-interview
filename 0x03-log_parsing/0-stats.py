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


def print_stats(total_size, status_codes):
    """
    Print statistics of parsed log entries.

    Args:
        total_size (int): Total sum of file sizes
        status_codes (dict): Count of HTTP status codes
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Process log entries from stdin and compute metrics."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                # Split line and extract relevant parts
                parts = line.split()
                # Verify line matches expected format
                if len(parts) > 2:
                    status = int(parts[-2])
                    file_size = int(parts[-1])
                    # Update metrics
                    if status in status_codes:
                        status_codes[status] += 1
                    total_size += file_size

            except (IndexError, ValueError):
                # Skip line if it doesn't match expected format
                pass

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_stats(total_size, status_codes)
        raise

    # Print final statistics if not interrupted
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

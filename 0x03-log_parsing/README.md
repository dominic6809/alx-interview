# 0x03. Log Parsing

## Overview
This project focuses on parsing and processing log data in real-time using Python. The primary objective is to read log entries from standard input, validate their format, and compute relevant metrics.

## Key Concepts
- **File I/O**: Reading from standard input line-by-line to handle large data efficiently.
- **Signal Handling**: Gracefully handling keyboard interruptions (CTRL + C) to provide summary statistics before exiting.
- **Data Processing**: Extracting relevant information from log entries using regular expressions and aggregating data.
- **Dictionaries**: Utilizing dictionaries to count occurrences of status codes and sum file sizes.
- **Exception Handling**: Managing potential errors during data processing to ensure smooth execution.

## Input Format
Log entries follow this specific format:

## Metrics Computed
After every 10 lines and upon keyboard interruption, the following statistics are printed:
- **Total file size**: The cumulative size of files processed.
- **Number of lines by status code**: Counts for the following status codes:
  - 200
  - 301
  - 400
  - 401
  - 403
  - 404
  - 405
  - 500

Status codes are displayed in ascending order.

## Usage
To generate random log entries, use the provided `0-generator.py` script. To parse and compute metrics, run the `0-stats.py` script with the generator as input:
```bash
./0-generator.py | ./0-stats.py
````

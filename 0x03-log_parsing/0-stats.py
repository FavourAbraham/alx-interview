#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print the statistics
def print_stats():
    global total_size
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        try:
            parts = line.split()
            # Check if the line is in the correct format
            if len(parts) < 7:
                continue

            # Extract the status code and file size from the line
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update the total file size
            total_size += file_size

            # Update the status code count if it's one of the expected codes
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with incorrect format or invalid values
            continue

    # Print final statistics after reading all input
    print_stats()

except KeyboardInterrupt:
    # Handle the case when the script is interrupted with CTRL + C
    print_stats()
    sys.exit(0)


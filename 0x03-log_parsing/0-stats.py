#!/usr/bin/python3
"""LOG PARSING"""
import sys
import signal


total_size = 0  # Sum of file sizes
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0}  # Status code counts
line_count = 0  # Line count tracker


def print_metrics():
    """Prints the total file size and status code metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_broken_pipe(signal, frame):
    """Handle broken pipe error silently."""
    print_metrics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGPIPE, handle_broken_pipe)


try:
    for line in sys.stdin:
        # Increment line count
        line_count += 1

        # extract streams into a list separated by spaces
        parts = line.split()

        # Validate line format
        if len(parts) < 7:
            continue  # skip

        # Extract relevant parts
        try:
            file_size = int(parts[-1])
            # Update total size
            total_size += file_size
        except ValueError:
            continue  # skip

        try:
            # extract status code -> second to last element
            status_code = int(parts[-2])
            # Update status code count
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            continue  # skip

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print_metrics()
    raise

# Print final metrics after loop ends
print_metrics()

#!/usr/bin/python3
"""LOG PARSING"""
import sys
import signal


def handle_broken_pipe(signal, frame):
    """Handle broken pipe error silently."""
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGPIPE, handle_broken_pipe)


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


try:
    for line in sys.stdin:
        parts = line.split()

        # Validate line format
        if len(parts) < 9:
            continue

        # Extract relevant parts
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size
            total_size += file_size

            # Update status code count
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Increment line count
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

        except (ValueError, IndexError):
            # Skip line if there's an error in parsing
            continue

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print_metrics()
    raise

# Print final metrics after loop ends
print_metrics()

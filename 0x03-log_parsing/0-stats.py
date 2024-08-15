#!/usr/bin/python3
"""Reads a script line by line and computes metrics"""
import sys
import signal


def print_stats(total_size, code_counts):
    """
    Defines a function to print total size
    & status code counts

    Args:
        total_size (int): total size of file in bytes
        code_counts (dict): number of status code counts

    Return:
        File size
        Status codes and their counts
        In ascending order
    """
    print("File size: {}".format(total_size))
    for code in sorted(code_counts.keys()):
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


def interrupt_handler(signal, frame):
    """
    Defines an interrupt handler
    After every 10 lines and/or a keyboard interruption
    """
    print_stats(total_size, code_counts)
    sys.exit(0)


# Register interrupt handler
signal.signal(signal.SIGINT, interrupt_handler)

total_size = 0
code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 9:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue

        if status_code in code_counts:
            code_counts[status_code] += 1

        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, code_counts)

except KeyboardInterrupt:
    interrupt_handler(signal.SIGINT, None)

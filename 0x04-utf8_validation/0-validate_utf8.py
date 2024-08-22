#!/usr/bin/python3
"""UTF-8 encoding"""


def validUTF8(data):
    """Validate utf-8 encoding of characters"""
    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep.startswith('110'):
                n_bytes = 1
            elif bin_rep.startswith('1110'):
                n_bytes = 2
            elif bin_rep.startswith('11110'):
                n_bytes = 3
            else:
                return False
        else:
            if not bin_rep.startswith('10'):
                return False
        n_bytes -= 1

    return n_bytes == 0

#!/usr/bin/python3
"""
module that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers where each integer represents a byte

    Returns:
        bool: True if data is valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & mask1) != 0:
                for i in range(5, 0, -1):
                    if byte & (1 << i):
                        num_bytes += 1
                    else:
                        break
                # UTF-8 allows only up to 4 bytes per character
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            # Check that the byte has the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0

#!/usr/bin/python3
"""
Module containing minOperations function to calculate
the fewest number of operations needed to achieve n characters
in a text file using only 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to
    result in exactly n 'H' characters using Copy All and Paste.

    Params:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
             If impossible, returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Perform factorization and count operations
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

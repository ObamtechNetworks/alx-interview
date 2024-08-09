#!/usr/bin/python3
"""Minimun Operations Problem"""


def minOperations(n) -> int:
    """The minimum operatiosn problem

    Args:
        n (integer): coin integer

    Returns:
        int: returns how many coins
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

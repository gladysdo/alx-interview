#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to
    result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed.
        Returns 0 if n is impossible to achieve.
    """

    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op

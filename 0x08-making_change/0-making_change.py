#!/usr/bin/python3
""" The coin change problem
To solve the change problem using dynamic programming.
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed to meet
    a given amount total.
    Args:
        coins (List[int]): list of coins denomination
        total (int): the given target amount to meet
    Returns:
       int: the fewest number of coins needed to meet
        a given amount total
    """
    if total <= 0:
        return 0
    # Initialize the dp array with a size of total + 1
    dp = [float("inf")] * (total + 1)  # set all elements to infintity
    dp[0] = 0  # No coins needed to make 0

    # Fill the dp table
    for c in coins:
        for i in range(c, total + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
    # Return resultvcheck dp[total]. If it's still infinity
    # it means the total cannot be reached with the given coins,
    # so return -1. Otherwise, return dp[total].
    return dp[total] if dp[total] != float('inf') else -1

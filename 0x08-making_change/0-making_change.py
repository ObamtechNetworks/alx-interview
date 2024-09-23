#!/usr/bin/python3
"""The coin change problem using a greedy algorithm."""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed to meet
    a given amount total using a greedy algorithm.

    Args:
        coins (List[int]): list of coin denominations
        total (int): the given target amount to meet

    Returns:
        int: the fewest number of coins needed to meet
        a given amount total
    """
    # If total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Sort coins in desc order to attempt the largest denomination first
    coins.sort(reverse=True)

    fewest = 0  # Counter for the fewest number of coins

    # Iterate over each coin denomination
    for coin in coins:
        if total == 0:
            break  # If total becomes 0, break out of the loop

        # Add the max number of coins of this denomination that can be used
        if coin <= total:
            # Calculate how many coins of this denomination
            num_of_coins = total // coin
            # Increment the fewest count by that number
            fewest += num_of_coins
            # Decrease the total by the equivalent value
            total -= num_of_coins * coin

    # If total is not 0 after the loop, return -1 (can't make exact change)
    return fewest if total == 0 else -1

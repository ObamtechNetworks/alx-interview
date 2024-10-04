#!/usr/bin/python3
"""The Prime Game
Finding a prime and utilizng
the Sieve of Erastothenes algorithm
"""


def sieve_of_eratosthenes(n):
    """Returns a list of booleans where True indicates
    the index is a prime number."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False
    return primes


def prime_count_up_to(n, sieve):
    """Returns the count of primes up to n using a precomputed sieve."""
    return sum(sieve[:n + 1])


def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.
    x: number of rounds
    nums: list of integers where each integer represents the size of the set
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)  # Get the maximum value of n in nums
    sieve = sieve_of_eratosthenes(max_n)  # Precompute primes up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = prime_count_up_to(n, sieve)

        # Maria wins if the number of prime removals is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

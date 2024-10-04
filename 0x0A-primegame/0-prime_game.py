#!/usr/bin/python3
"""The Prime Game
Finding a prime and utilizng
the Sieve of Erastothenes algorithm
"""


def sieve_of_eratosthenes(n):
    """Returns a list of booleans indicating whether
    numbers from 0 to n are prime.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False

    return primes


def play_game(n, primes):
    """
    Simulates the game for a given n using precomputed primes.
    Returns 1 if Maria wins, 0 if Ben wins.
    """
    numbers = list(range(n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        prime_found = False
        # Debug statement to trace the game
        # print(f"Game for n = {n}, Current Turn:
        # {'Maria' if turn == 0 else 'Ben'}")

        # Find the next available prime number
        for i in range(2, n + 1):
            if numbers[i] != 0 and primes[i]:
                prime_found = True
                # Debug statement to show the prime picked
                # print(f"Prime {i} picked by
                # {'Maria' if turn == 0 else 'Ben'}")
                # Remove the prime and its multiples
                for j in range(i, n + 1, i):
                    numbers[j] = 0
                break

        if not prime_found:
            # Debug statement to indicate no primes left
            # print(f"No primes left,
            # {'Maria' if turn == 0 else 'Ben'} cannot move.")
            break

        # Switch turns
        turn = 1 - turn

    # Determine the winner
    if turn == 0:
        # It's Maria's turn, she cannot move, so Ben wins
        return 0
    else:
        # It's Ben's turn, he cannot move, so Maria wins
        return 1


def isWinner(x, nums):
    """Determines the overall winner after x rounds."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        # Debug statement to show the winner of the round
        # print(f"Round for n={n}: {'Maria' if winner == 1 else 'Ben'} wins")

        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # print(f"Total: Maria {maria_wins}, Ben {ben_wins}")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

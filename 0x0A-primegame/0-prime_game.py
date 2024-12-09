#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """
        Generate a list of primes up to n using the Sieve of Eratosthenes
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def game_round(n):
        """Simulate the game for a given value of n"""
        primes = sieve_of_eratosthenes(n)
        primes_left = primes[:]
        turn = 0  # Maria starts, turn = 0 for Maria, 1 for Ben

        while primes_left:
            current_prime = primes_left.pop(0)
            # Remove multiples of the current prime from the remaining primes
            primes_left = [p for p in primes_left if p % current_prime != 0]
            # Switch turn
            turn = 1 - turn

        # If turn is 0, that means it was Ben's turn last, so Maria won
        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_round(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

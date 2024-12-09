# 0x0A-primegame
# Prime Game Winner

## Description

In this game, two players, Maria and Ben, take turns selecting a prime number from a set of consecutive integers starting from 1 to `n`. After a prime number is selected, it and its multiples are removed from the set. The player who cannot make a move (i.e., there are no primes left to choose) loses. Maria always starts first, and both players play optimally.

The task is to determine who wins the most rounds from a list of game rounds, each defined by a value of `n`.

## Function Prototype

```python
def isWinner(x, nums):
    """
    Args:
        x (int): Number of rounds played.
        nums (list of int): List of n values for each round.
        
    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben").
        None: If both players won an equal number of rounds.
    """
```
## Approach

### Prime Generation:
Using the Sieve of Eratosthenes algorithm to efficiently identify all prime numbers up to `n` for each game round.

### Game Simulation:
- Maria picks the smallest available prime, removes it and its multiples.
- Ben follows the same strategy, and the game ends when no prime numbers remain.

### Optimal Play:
- Players always play optimally by picking the smallest remaining prime.
- The player who cannot pick a prime loses the round.

### Counting Wins:
After each round, count how many rounds each player wins. Return the player with the most wins, or `None` if they tie.

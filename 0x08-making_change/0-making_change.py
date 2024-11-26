#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a total amount
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1

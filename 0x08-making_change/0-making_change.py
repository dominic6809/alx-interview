#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a total amount
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    remainder = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_idx >= n:
            return -1
        if remainder - sorted_coins[coin_idx] >= 0:
            remainder -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count

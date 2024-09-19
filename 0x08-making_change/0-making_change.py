#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[total] != float('inf'):
            break

    return dp[total] if dp[total] != float('inf') else -1

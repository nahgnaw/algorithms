# -*- coding: utf-8 -*-

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    # DP.
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if not amount:
            return 0
            
        # dp[i]: the fewest number of coins for amount i.
        dp = [0] + [float('inf')] * (amount)
        
        for i in xrange(1, amount + 1):
            # dp[i] = min{dp[i - coins[j]]} (0 <= j < len(coins))
            dp[i] = min([dp[i - coin] if i >= coin else float('inf') for coin in coins]) + 1
        
        return dp[-1] if not dp[-1] == float('inf') else -1
        
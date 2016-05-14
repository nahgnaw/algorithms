# -*- coding: utf-8 -*-

"""
How can a given amount of money be made with the least number of coins of given denominations?
"""


class Solution(object):
    # dp[i]: the minimum number of coins for amount i
    def make_change(self, coin_values, target):
        dp = [0] * (target + 1)
        for c in [c for c in coin_values if c <= target]:
            dp[c] = 1

        for i in xrange(1, target + 1):
            for c in [c for c in coin_values if c < i]:
                if not dp[i] or dp[i] > dp[i-c] + 1:
                    dp[i] = dp[i-c] + 1 if dp[i-c] else 0
        return dp[-1] if dp[-1] else None

    # Return the number of each coin value.
    # dp[i]: the coins for amount i.
    def make_change2(self, coin_values, target):
        dp = [[] for _ in xrange(target + 1)]
        for c in [c for c in coin_values if c <= target]:
            dp[c].append(c)

        for i in xrange(1, target + 1):
            for c in [c for c in coin_values if c < i]:
                if not dp[i] or len(dp[i]) > len(dp[i-c]) + 1:
                    dp[i] = dp[i-c] + [c] if dp[i-c] else []
        return sorted(dp[-1]) if dp[-1] else None


if __name__ == '__main__':
    sol = Solution()
    coin_values = [2,5,10]
    target = 7
    print sol.make_change2(coin_values, target)

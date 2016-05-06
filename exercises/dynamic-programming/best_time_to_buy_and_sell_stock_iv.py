# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k or not prices:
            return 0
            
        # If k is larger than half of the given days, it means
        # we can have as many transactions as we want since
        # one transaction takes two days to complete. 
        if k > len(prices) / 2:
            profit = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
            
        # buy[j]: the max profit after buying the stock for the jth time
        buy = [float('-inf')] * k
        # sell[j]: the max profit after selling the stock for the jth time
        sell = [0] * k
        for p in prices:
            for j in xrange(k-1, -1, -1):
                sell[j] = max(sell[j], buy[j] + p)
                buy[j] = max(buy[j], (sell[j-1] if j > 0 else 0) - p)
        return sell[-1]
        


if __name__ == '__main__':
    k = 1
    prices = [2, 1]
    sol = Solution()
    print sol.maxProfit(k, prices)
        
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        buy = float('-inf') # The max profit after buying the stock
        sell = 0            # The max profit after selling the stock
        for p in prices:
            sell = max(sell, buy + p)
            buy = max(buy, -p)
        return sell

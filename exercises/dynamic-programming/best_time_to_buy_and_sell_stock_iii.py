# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
            
        # buy1: the max profit after buying the first stock
        # buy2: the max profit after buying the second stock
        buy1 = buy2 = float('-inf')
        # sell1: the max profit after selling the first stock
        # sell2: the max profit after selling the second stock
        sell1 = sell2 = 0
        for p in prices:
            sell2 = max(sell2, buy2 + p)
            buy2 = max(buy2, sell1 - p)
            sell1 = max(sell1, buy1 + p)
            buy1 = max(buy1, -p)
        return sell2
        
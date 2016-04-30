# -*- coding: utf-8 -*-

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):
    """
        Trailing zeros in n! can only be produced by 2 * 5.
        So we need to find out how many 2's and 5's n! can be decomposed into.
        Since there are more 2's than 5's, we only need to find out how many 5's n! can be decomposed into.
    """
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            n /= 5
            result += n
        return result



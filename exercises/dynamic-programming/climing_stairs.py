# -*- coding: utf-8 -*-

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution(object):
    # O(n) space
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        res = [1] * (n + 1)
        res[1] = 1
        for i in xrange(2, n + 1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

    # O(1) space
    def climbStairs2(self, n):
        if n < 1:
                return 0

        i = j = 1
        for _ in xrange(n-1):
            i, j = j, i + j
            
        return j
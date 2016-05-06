# -*- coding: utf-8 -*-

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m and not n:
            return 0
            
        # dp[i][j]: the number of unique paths from the top-left corner to [i,j].
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                # There will not be one path if the destination is on the edges.
                if not i or not j:
                    dp[i][j] = 1
                else:
                    # A cell can only be reached from left or from top.
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths2(self, m, n):
        if m > n:
            return self.uniquePaths2(n, m)

        if not m or not n:
            return 0

        sol = [1 for i in xrange(m)]

        for j in xrange(1, n):
            for i in xrange(1, m):
                sol[i] = sol[i] + sol[i-1]

        return sol[-1]
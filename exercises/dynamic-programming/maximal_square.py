# -*- coding: utf-8 -*-

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

class Solution(object):
    """
    dp[i][j]: the edge length of the maximal square with the bottom right vertex at (i,j). 
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        dp = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        max_area = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j] and i and j:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                max_area = max(max_area, dp[i][j] ** 2)
        return max_area

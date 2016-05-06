# -*- coding: utf-8 -*-

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def walk(i, j, val):
            # Out of boundaries.
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]):
                return 0
            
            # Not increasing.    
            if val >= matrix[i][j]:
                return 0
            
            # Not computed before.
            if not dp[i][j]:    
                dp[i][j] = 1 + max(
                    walk(i - 1, j, matrix[i][j]),
                    walk(i + 1, j, matrix[i][j]),
                    walk(i, j - 1, matrix[i][j]),
                    walk(i, j + 1, matrix[i][j])
                )
            return dp[i][j]
        
        if not matrix or not matrix[0]:
            return 0
            
        result = 0
        dp = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                result = max(result, walk(i, j, float('-inf')))
        return result


if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    sol = Solution()
    print sol.longestIncreasingPath(matrix)

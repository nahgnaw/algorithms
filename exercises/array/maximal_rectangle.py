# -*- coding: utf-8 -*-

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""


class Solution(object):
    """
    The solution is based on largest rectangle in histogram solution. Every row in the matrix is viewed as the ground with some buildings on it. The building height is the count of consecutive 1s from that row to above rows. The rest is then the same as this solution for largest rectangle in histogram
    """
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_rec = 0
        m = len(matrix[0])
        heights = [0] * (m + 1) # Extra 0 in the end
        
        for row in matrix:
            for i in xrange(m):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
                
            stack = [-1]
            for i in xrange(m + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_rec = max(max_rec,  h * w)
                stack.append(i)
        return max_rec

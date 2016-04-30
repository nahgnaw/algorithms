# -*- coding: utf-8 -*-

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
            
        matrix = [[None for _ in xrange(n)] for _ in xrange(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        while left < right and top < bottom:
            # Go right
            for i in xrange(left, right):
                matrix[top][i] = num
                num += 1

            # Go down
            for i in xrange(top, bottom):
                matrix[i][right] = num
                num += 1

            # Go left
            for i in xrange(right, left, -1):
                matrix[bottom][i] = num
                num += 1

            # Go up
            for i in xrange(bottom, top, -1):
                matrix[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        # A single spot
        if left == right and top == bottom:
            matrix[left][top] = num

        return matrix
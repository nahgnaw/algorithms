# -*- coding: 8tf8 -*-

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left < right and top < bottom:
            # Go right
            for i in xrange(left, right):
                result.append(matrix[top][i])

            # Go down
            for i in xrange(top, bottom):
                result.append(matrix[i][right])

            # Go left
            for i in xrange(right, left, -1):
                result.append(matrix[bottom][i])

            # Go up
            for i in xrange(bottom, top, -1):
                result.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        # A single spot
        if left == right and top == bottom:
            result.append(matrix[left][top])

        # A single row
        elif top == bottom:
            for i in xrange(left, right + 1):
                result.append(matrix[top][i])

        # A single column
        elif left == right:
            for i in xrange(top, bottom + 1):
                result.append(matrix[i][left])

        return result


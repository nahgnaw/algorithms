# -*- coding: utf-8 -*-

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        # Transpose
        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i]) / 2):
                matrix[i][j], matrix[i][len(matrix[i]) - 1 - j] = matrix[i][len(matrix[i]) - 1 - j], matrix[i][j]
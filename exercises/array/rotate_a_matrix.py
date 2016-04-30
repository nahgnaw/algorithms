# -*- coding: utf-8 -*-

"""
Rotate a square matrix.
"""


class Solution(object):
    def clockwise_90(self, matrix):
        # First transpose, then reverse each row. 
        # In-place.
        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i]) / 2):
                matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

    def counterclockwise_90(self, matrix):
        # First transpose, then reverse each column. 
        # In-place.
        for i in xrange(len(matrix)):
            for j in xrange(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(len(matrix[0])):
            for j in xrange(len(matrix) / 2):
                matrix[j][i], matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - j - 1][i], matrix[j][i]

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print matrix
    sol = Solution()
    # sol.clockwise_90(matrix)
    # print matrix
    sol.counterclockwise_90(matrix)
    print matrix


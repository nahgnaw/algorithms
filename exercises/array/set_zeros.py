# -*- coding: utf-8 -*-

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    # Space O(m+n)
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        row_ind, col_ind = set(), set()  # Keep the indecies that should be set to zero.
        for i in xrange(m):
            for j in xrange(n):
                if not matrix[i][j]:
                    row_ind.add(i)
                    col_ind.add(j)
            
        # Set zeros.        
        for i in row_ind:
            matrix[i] = [0] * n
        for j in col_ind:
            for i in xrange(m):
                matrix[i][j] = 0

    # Space O(1)
    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        # row0 is 0 if any element in the first row is zero
        row0 = 0 if any([matrix[0][i] == 0 for i in xrange(n)]) else 1
        # col0 is 0 if any elment in the first column is zero
        col0 = 0 if any([matrix[j][0] == 0 for j in xrange(m)]) else 1
        # Put the states of other columns in matrix[0][1:].
        # Put the states of other rows in matrix[1:][0].
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in xrange(1, m):
            if not matrix[i][0]:
                matrix[i] = [0] * n
        for j in xrange(1, n):
            if not matrix[0][j]:
                for i in xrange(m):
                    matrix[i][j] = 0
        if not row0:
            matrix[0] = [0] * n
        if not col0:
            for i in xrange(m):
                matrix[i][0] = 0
            
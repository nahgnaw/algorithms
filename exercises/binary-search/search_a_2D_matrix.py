# -*- coding: utf-8 -*-

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid / n][mid % n] == target:
                return True
            elif matrix[mid / n][mid % n] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                start = mid + 1
            else:
                end = mid - 1

        row_num = start

        start, end = 0, len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) / 2
            if matrix[row_num][mid] == target:
                return True
            elif matrix[row_num][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False


if __name__ == '__main__':
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 12
    sol = Solution()
    print sol.searchMatrix2(matrix, target)

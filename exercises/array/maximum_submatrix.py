# -*- coding: utf-8 -*-

"""
Given a 2D array, find the maximum sum submatrix in it. For example, in the following 2D array, 

[
    [1,  2,  -1, -4, -20],
    [-8, -3, 4,  2,  1],
    [3,  8,  10, 1,  3],
    [-4, -1, 1,  7, -6]
]

the maximum sum submatrix is the rectangle from (1,1) to (3,3) and sum of this submatrix is 29.
"""


class Solution(object):
    # O(n^3)
    def max_submatrix(self, matrix):

        def max_subarray(nums):
            max_sum = cur_sum = nums[0]
            max_left = max_right = 0
            cur_left = 0

            for i in xrange(1, len(nums)):
                if cur_sum + nums[i] > nums[i]:
                    cur_sum += nums[i]
                else:
                    cur_sum = nums[i]
                    cur_left = i

                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_left = cur_left
                    max_right = i

            return max_sum, max_left, max_right

        max_sum = matrix[0][0]
        max_left, max_right, max_top, max_bottom = 0, 0, 0, 0
        for left in xrange(len(matrix[0])):
            # Crate an array contains the row sum from column left to column right.
            # Apply max_subarray on this array column by column from left to right.
            temp = [0] * len(matrix)
            for right in xrange(left, len(matrix[0])):
                for row in xrange(len(matrix)):
                    temp[row] += matrix[row][right]

                cur_sum, top, bottom = max_subarray(temp)
                # Update max_sum when necessary.
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_left, max_right, max_top, max_bottom = left, right, top, bottom

        return max_sum, max_left, max_right, max_top, max_bottom


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1,  2,  -1, -4, -20],
        [-8, -3, 4,  2,  1],
        [3,  8,  10, 1,  3],
        [-4, -1, 1,  7, -6]
    ]
    print sol.max_submatrix(matrix)

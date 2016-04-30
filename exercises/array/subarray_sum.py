# -*- coding: utf-8 -*-

"""
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    # O(n)
    def subarraySum(self, nums):
        sum_map = {0: 0}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum in sum_map:
                return [sum_map[sum], i]
            else:
                sum_map[sum] = i + 1


if __name__ == '__main__':
    nums = [1, -3, 1, 2, -3, 4]
    sol = Solution()
    print sol.subarraySum(nums)

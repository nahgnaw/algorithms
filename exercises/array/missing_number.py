# -*- coding: utf-8 -*-

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution(object):
    # XOR
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in xrange(len(nums)):
            result ^= i
            result ^= nums[i]
        return result

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(nums)):
            result += i + 1
            result -= nums[i]
        return result
        
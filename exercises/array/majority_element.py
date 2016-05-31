# -*- coding: utf-8 -*-

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    # Time: O(n). Space: O(n).
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1
            if counts[x] > len(nums) / 2:
                return x

    # Moore voting algorithm
    # Time: O(n). Space: O(1).
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = None, 0
        for x in nums:
            if count == 0:
                majority = x
                count = 1
            elif x == majority:
                count += 1
            else:
                count -= 1
        return majority

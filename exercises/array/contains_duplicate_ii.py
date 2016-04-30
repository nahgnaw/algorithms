# -*- coding: utf-8 -*-

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
that nums[i] = nums[j] and the difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not len(nums):
            return False
        d = {}
        for ind, val in enumerate(nums):
            if val not in d:
                d[val] = ind
            elif ind - d[val] <= k:
                return True
            else:
                d[val] = ind
        return False

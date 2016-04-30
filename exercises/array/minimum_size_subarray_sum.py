# -*- coding: utf-8 -*-

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution(object):
    # Use two pointers to maintain a window. Expand the window if sum >= s, shrink the window otherwise.
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
            
        min_len = float('inf')
        left, right = 0, 1
        while right <= len(nums):
            if sum(nums[left:right]) < s:
                right += 1
            else:
                if right - left == 1:
                    return 1
                else:
                    min_len = min(min_len, right - left)
                    left += 1
                    
        if min_len == float('inf'):
            return 0
        return min_len

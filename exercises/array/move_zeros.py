# -*- coding: utf-8 -*-

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Move i to the first zero element
        i = 0
        while i < len(nums):
            if not nums[i]:
                break
            i += 1
        
        # If the array is exhausted, just return
        if i == len(nums):
            return
        
        # Swap zeros to the end        
        j = i + 1
        while j < len(nums):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
                
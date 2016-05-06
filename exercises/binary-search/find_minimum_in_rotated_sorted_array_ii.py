# -*- coding: utf-8 -*-

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while nums[left] == nums[right] and left < right:
            right -= 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left] 
            mid = left + (right - left) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
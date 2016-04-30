# -*- coding: utf-8 -*-

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        left = 0
        while left < len(nums):
            step = 1
            while left + step < len(nums) and nums[left+step] == nums[left] + step:
                step += 1
            if step > 1:
                result.append(str(nums[left]) + '->' + str(nums[left+step-1]))
            else:
                result.append(str(nums[left]))
            left += step
        return result



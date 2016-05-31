# -*- coding: utf-8 -*-

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        # There will be at most two mojority elements that appear more than n/3 times.
        majority_1, majority_2 = None, None
        count_1, count_2 = 0, 0
        for x in nums:
            if x == majority_1:
                count_1 += 1
            elif x == majority_2:
                count_2 += 1
            elif count_1 == 0:
                majority_1 = x
                count_1 = 1
            elif count_2 == 0:
                majority_2 = x
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        
        result = set()
        count_1, count_2 = 0, 0
        for x in nums:
            if x == majority_1:
                count_1 += 1
                if count_1 > len(nums) / 3:
                    result.add(majority_1)
            elif x == majority_2:
                count_2 += 1
                if count_2 > len(nums) / 3:
                    result.add(majority_2)
        return list(result)
                    
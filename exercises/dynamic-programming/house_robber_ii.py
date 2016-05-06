# -*- coding: utf-8 -*-

"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(start, end):
            last = 0    # max money robbed from last house
            now = 0     # max money robbed from current house
            for x in nums[start:end+1]:
                last, now = now, max(last + x, now)
            return now
            
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # Either rob from house 0 to house n-2, or from house 1 to house n-1.    
        return max(_rob(0, len(nums) - 2), _rob(1, len(nums) - 1))
        
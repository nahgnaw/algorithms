# -*- coding: utf-8 -*-

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
    # Space: O(n)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]
            
        #dp[i]: the maximum amount of money that can be robbed after robbing house i
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

    # Space: O(1)
    def rob2(self, nums):
        last = 0    # max money robbed from last house
        now = 0     # max money robbed from current house
        for x in nums:
            last, now = now, max(last + x, now)
        return now
        
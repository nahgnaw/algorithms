# -*- coding: utf-8 -*-

"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map = {0: -1}
        sum = 0
        max_len = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum not in sum_map:
                sum_map[sum] = i
            if sum - k in sum_map:
                max_len = max(max_len, i - sum_map[sum-k])
        return max_len 
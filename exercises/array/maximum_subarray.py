# -*- coding: utf-8 -*-

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    """
    res[i]: the max subarray sum that ends with nums[i].
    res[i] = max(nums[i] + res[i-1], nums[i]) (or res[i] = nums[i] + res[i-1] if res[i-1] > 0 else nums[i])
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * len(nums)
        max_sum = res[0] = nums[0]
        for i in xrange(1, len(nums)):
            res[i] = max(nums[i] + res[i-1], nums[i])
            max_sum = max(max_sum, res[i])
        return max_sum
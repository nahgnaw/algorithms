# -*- coding: utf-8 -*-

"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
            
        result = 0
        nums.sort() # Soring is allowed because only index triple count is required.
        for i in xrange(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < target - nums[i]:
                    result += k - j
                    j += 1
                else:
                    k -= 1
        return result

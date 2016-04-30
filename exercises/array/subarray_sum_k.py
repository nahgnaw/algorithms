# -*- coding -*-

"""
Given an nonnegative integer array, find a subarray where the sum of numbers is k.
Your code should return the index of the first number and the index of the last number.

Example
Given [1, 4, 20, 3, 10, 5], sum k = 33, return [2, 4].
"""


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums, k):
        sum_map = {0: 0}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum - k in sum_map:
                return [sum_map[sum-k], i]
            else:
                sum_map[sum] = i + 1
        return []


if __name__ == '__main__':
    nums = [1, 4, 20, 3, 10, 5]
    k = 33
    sol = Solution()
    print sol.subarraySum(nums, k)
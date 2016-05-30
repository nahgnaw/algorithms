# -*- coding: utf-8 -*-

"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for ind, val in enumerate(nums):
            if val in d:
                return sorted([d[val] + 1, ind + 1])
            else:
                d[target - val] = ind
        return [0, 0]

if __name__ == '__main__':
    nums = [1, 4, 2]
    target = 6
    sol = Solution()
    print sol.twoSum(nums, target)

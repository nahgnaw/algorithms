# -*- coding: utf-8 -*-

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(pos, tmp, target):
            if target < 0 or len(tmp) > k:
                return
            if target == 0 and len(tmp) == k:
                result.append(tmp)
                return
            
            for i in xrange(pos, len(nums)):
                dfs(i + 1, tmp + [nums[i]], target - nums[i])
        
        result = []
        nums = range(1, 10)
        dfs(0, [], n)
        return result
        
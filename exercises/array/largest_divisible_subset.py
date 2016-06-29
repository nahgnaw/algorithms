# -*- coding: utf-8 -*-

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        nums.sort()
        largest_subset = []
        for i in xrange(len(nums)):
            temp = []
            temp.append(nums[i])
            # Look backward
            for j in xrange(i-1, -1, -1):
                if not temp[0] % nums[j]:
                    temp.insert(0, nums[j])
            # Look forward
            for j in xrange(i + 1, len(nums)):
                if not nums[j] % temp[-1]:
                    temp.append(nums[j])
            if len(temp) > len(largest_subset):
                largest_subset[:] = temp
                
        return largest_subset

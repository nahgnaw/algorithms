# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):
    # Using set
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums)
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                longest = max(longest, y - x)
        return longest

    # Using dictionary
    def longestConsecutive2(self, nums):
        longest = 0
        d = {}
        for n in nums:
            if n not in d:
                # Look for neighbors of n. 
                # If there is any neighbor, compute the sequence length and set the length as the value of d[n].
                left = d.get(n - 1, 0)
                right = d.get(n + 1, 0)
                length = left + right + 1
                d[n] = length
                longest = max(longest, length)
                # Update the value of the sequence boundary elements.
                d[n-left] = d[n+right] = length
        return longest



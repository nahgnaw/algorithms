# -*- coding: utf-8 -*-

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_result = 0
        for i in nums:
            xor_result ^= i

        # Get the rightmost bit which is 1
        rightmost_one_bit = xor_result & -xor_result

        # Use the rightmost_one_bit to separate nums
        single_one = single_two = 0
        for i in nums:
            if rightmost_one_bit & i:
                single_one ^= i
            else:
                single_two ^= i

        return [single_one, single_two]
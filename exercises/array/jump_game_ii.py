# -*- coding: utf-8 -*-

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_jump_max, next_jump_max, step_count = 0, 0, 0
        for i in xrange(len(nums) - 1):
            next_jump_max = max(next_jump_max, i + nums[i])
            if i == curr_jump_max:
                step_count += 1
                curr_jump_max = next_jump_max
        return step_count
        
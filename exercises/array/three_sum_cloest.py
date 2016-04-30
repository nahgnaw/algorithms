# -*- coding: utf-8 -*-

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = nums[0] + nums[1] + nums[2] - target

        for i in xrange(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = sum - target
                if diff == 0:
                    return sum
                min_diff = diff if abs(min_diff) > abs(diff) else min_diff
                if diff < 0:
                    j += 1
                else:
                    k -= 1

        return min_diff + target


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    print sol.threeSumClosest(nums, target)
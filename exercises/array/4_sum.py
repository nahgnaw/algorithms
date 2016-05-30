# -*- coding: utf-8 -*-

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        if not nums or len(nums) < 4:
            return res

        nums = sorted(nums)
        for i in xrange(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(len(nums) - 1, i + 2, -1):
                if j < len(nums) - 1 and nums[j] == nums[j+1]:
                    continue
                k = i + 1
                s = j - 1
                while k < s:
                    sum = nums[i] + nums[k] + nums[s] + nums[j]
                    if sum == target:
                        res.append((nums[i], nums[k], nums[s], nums[j]))
                        while k < s and nums[k] == nums[k+1]:
                            k += 1
                        while k < s and nums[s] == nums[s-1]:
                            s -= 1
                        k += 1
                        s -= 1
                    elif sum < target:
                        k += 1
                    else:
                        s -= 1

        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    res = sol.fourSum(nums, target)
    for r in res:
        print r

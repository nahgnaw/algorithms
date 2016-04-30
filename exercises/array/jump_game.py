# -*- coding: utf-8 -*- 

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    def canJump(self, nums):
        # res[i]: whether i can be reached
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = [False for _ in xrange(len(nums))]
        res[0] = True
        for i in xrange(len(nums)):
            for j in xrange(i):
                if j + nums[j] >= i and res[j]:
                    res[i] = True
        return res[-1]

    # Greedy. Bottom-up.
    def canJump2(self, nums):
        ind = len(nums) - 1
        for i in xrange(len(nums) - 1, -1, -1):
            if i + nums[i] >= ind:
                ind = i
        return ind == 0


if __name__ == '__main__':
    nums = [2, 0]
    sol = Solution()
    print sol.canJump2(nums)


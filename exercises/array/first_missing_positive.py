# -*- coding: utf-8 -*-

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):
    # Bucket sort. Put nums[i] - 1 at i. 
    # O(n)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 1

        for i in xrange(n):
            while True:
                if nums[i] <=0 or nums[i] > n or nums[i] == nums[nums[i]-1]:
                    break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in xrange(n):
            if not nums[i] - 1 == i:
                return i + 1
        return n + 1


if __name__ == '__main__':
    nums = [3,4,-1,1]
    sol = Solution()
    print sol.firstMissingPositive(nums)

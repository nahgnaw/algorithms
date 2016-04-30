# -*- coding: utf-8 -*-

"""
Given an array of n integers ranging from 1 to n. There is one missing value and one duplicate. Find the duplicate.

E.g. [1,3,4,3]. Return 3
"""


class Solution(object):
    def find_duplicate(self, nums):
        if len(nums) < 2:
            return None

        for i in xrange(len(nums)):
            while True:
                if nums[i] == nums[nums[i]-1]:
                    break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in xrange(len(nums)):
            if not nums[i] == i + 1:
                return nums[i]



if __name__ == '__main__':
    sol = Solution()
    nums = [2,1,4,2]
    print sol.find_duplicate(nums)

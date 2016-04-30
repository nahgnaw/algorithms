# -*- coding: utf-8 -*-

"""
Given a list of integers, which denote a permutation.
Find the previous permutation in ascending order.

Example:
For [1,3,2,3], the previous permutation is [1,2,3,3]
For [1,2,3,4], the previous permutation is [4,3,2,1]
"""


class Solution(object):
    """
    1. Loop over the list from the right-hand side, if all the elements is ordered decreasingly, just return the reversed list.
    2. Starting from the right-hand side, find the first element (named A) that breaks the decreasing order.
    3. Starting from the right-hand side, find the first element (named B) that is smaller than A. Swap A and B.
    4. Reverse all the elements on the right of the position of current A.
    """
    def previousPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 1:
            return

        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] > nums[i+1]:
                break
            elif i == 0:
                nums[:] = nums[::-1]
                return

        for j in xrange(len(nums) - 1, i, -1):
            if nums[j] < nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:len(nums)] = nums[len(nums)-1:i:-1]


if __name__ == '__main__':
    nums = [2,2,1]
    sol = Solution()
    sol.previousPermutation(nums)
    print nums
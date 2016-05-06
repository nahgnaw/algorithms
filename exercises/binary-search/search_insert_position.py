# -*- coding: utf-8 -*-

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left



if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    sol = Solution()
    print sol.searchInsert(nums, target)
    print sol.searchInsert2(nums, target)


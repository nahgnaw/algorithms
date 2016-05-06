# -*- coding: utf-8 -*-

"""
Find a value in sorted array. If found, return its index. If not found, return none.
"""


class Solution(object):
    def search(self, nums, x):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == x:
                return mid
            elif nums[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return None


if __name__ == '__main__':
    sol = Solution()
    nums = [-3, -2, 0, 1, 8, 9]
    x = 0
    print sol.search(nums, x)

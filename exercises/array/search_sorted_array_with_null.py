# -*- coding: utf-8 -*-

"""
Given a sorted int array, replace some of the elements with null. Search for a value x, return its index. If it is not in the array, return -1.
"""


class Solution(object):
    def search(self, nums, x):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if not nums[mid] is None:
                if nums[mid] == x:
                    return mid
                elif nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                l = r = mid
                while l > 0 and nums[l] is None:
                    l -= 1
                while r < len(nums) - 1 and nums[r] is None:
                    r += 1
                if nums[l] < x < nums[r]:
                    return -1
                if nums[l] == x:
                    return l
                elif nums[l] > x:
                    right = l - 1
                if nums[r] == x:
                    return r
                elif nums[r] < x:
                    left = r + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [2,None,6,None]
    x = 2
    print sol.search(nums, x)

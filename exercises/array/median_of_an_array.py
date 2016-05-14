# -*- coding: utf-8 -*-

"""
Given an unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example
Given [4, 5, 1, 2, 3], return 3

Given [7, 9, 4, 5], return 5

Challenge
O(n) time.
"""


class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):

        def quick_select(left, right, k):
            if left >= right:
                return nums[left]

            l, r = left, right
            pivot = left
            while l < r:
                while l < r and nums[r] >= nums[pivot]:
                    r -= 1
                while l < r and nums[l] <= nums[pivot]:
                    l += 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[left], nums[l] = nums[l], nums[left]

            if l + 1 == k:
                return nums[l]
            elif l + 1 < k:
                return quick_select(l + 1, right, k)
            else:
                return quick_select(left, l - 1, k)
                
        # For array with the odd number of elements, 
        # the median is the (N+1)/2-th smallest number
        # For array with the even number of elements, 
        # the median is also the (N+1)/2-th smallest number, as (N+1)/2 == N/2 
        return quick_select(0, len(nums) - 1, (len(nums) + 1) / 2)


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,-6,-7]
    print sol.median(nums)


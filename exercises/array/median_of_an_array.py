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
        
        def find_kth_smallest(left, right, k):
            if left == right:
                return nums[left]
                
            walk = left
            anchor = nums[left]
            for i in xrange(left + 1, right + 1):
                if nums[i] <= anchor:
                    walk += 1
                    nums[walk], nums[i] = nums[i], nums[walk]
            nums[left], nums[walk] = nums[walk], nums[left]
            
            if walk - left + 1 == k:
                return nums[walk]
            elif walk - left + 1 > k:
                return find_kth_smallest(left, walk - 1, k)
            else:
                return find_kth_smallest(walk + 1, right, k - (walk - left + 1))
                
        # For array with the odd number of elements, 
        # the median is the (N+1)/2-th smallest number
        # For array with the even number of elements, 
        # the median is also the (N+1)/2-th smallest number, as (N+1)/2 == N/2 
        return find_kth_smallest(0, len(nums) - 1, (len(nums) + 1) / 2)

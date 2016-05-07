# -*- coding: utf-8 -*-

"""
Given a sorted array and a threshold, return the median of the sub-array whose elements are no smaller than the threshold.
"""


class Solution(object):
    def get_median(self, nums, threshold):
        if not nums:
            return None
        if threshold > nums[-1]:
            return None

        # Search for the first element that is no smaller than the threshold.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            # When equality happens, we want to keep searching towards the left in case of duplicates.
            if nums[mid] >= threshold:
                right = mid - 1
            else:
                left = mid + 1
        # Now left is the index of the first element that is no smaller than the threshold.
        length = len(nums[left:])
        if length % 2:
            return nums[left+length/2]
        return (nums[left+(length-1)/2] + nums[left+length/2]) / 2.0


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,4,4,5,7,8,9,9,12]
    threshold = 13
    print sol.get_median(nums, threshold)

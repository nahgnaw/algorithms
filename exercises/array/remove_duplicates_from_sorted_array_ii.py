# -*- coding: utf-8 -*-

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    # Two pointers
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        i = 0
        for j in xrange(len(nums)):
            if i < 2 or not nums[j] == nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i


    def removeDuplicates2(self, nums):
        k = 2

        if len(nums) < k:
            return len(nums)

        # count: number of duplicates
        i = j = count = 1
        while j < len(nums):
            if not nums[j] == nums[j-1]:
                count = 1
                nums[i] = nums[j]
                i += 1
            else:
                if count < k:
                    count += 1
                    nums[i] = nums[j]
                    i += 1
            j += 1
        return i

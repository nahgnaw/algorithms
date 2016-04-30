# -*- coding: utf-8 -*-

"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    # Move all the elements equal to val to the end of the array, then remove them
    # O(n)
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        length = len(nums)
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
                continue
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        for k in xrange(length - j - 1):
            nums.pop()
        return len(nums)


if __name__ == '__main__':
    nums = [1]
    val = 1
    sol = Solution()
    print sol.removeElement(nums, val)

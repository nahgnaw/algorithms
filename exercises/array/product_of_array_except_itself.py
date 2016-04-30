# -*- coding: utf-8 -*-

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution(object):
    # Time: O(n). Space: O(n)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        l, r = 1, len(nums) - 2
        while l < len(nums) and r > -1:
            left[l] = left[l-1] * nums[l-1]
            right[r] = right[r+1] * nums[r+1]
            l += 1
            r -= 1

        return [left[i] * right[i] for i in xrange(len(nums))]


    # Time: O(n). Space: O(1)
    def productExceptSelf2(self, nums):
        result = [1] * len(nums)
        for i in xrange(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        tmp = 1
        for i in xrange(len(nums) - 1, -1, -1):
            result[i] *= tmp
            tmp *= nums[i]
        return result


if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    print sol.productExceptSelf(nums)
    print sol.productExceptSelf2(nums)

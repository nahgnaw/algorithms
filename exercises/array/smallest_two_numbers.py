# -*- coding: utf-8 -*-

"""
Find the smallest and the second smallest numbers of an integer array.
"""

class Solution(object):
    def smallest_numbers(self, nums):
        if len(nums) < 2:
            return None

        a, b = nums[0], nums[1]
        if a > b:
            a, b = b, a

        for x in nums[2:]:
            if x < a:
                a, b = x, a
            elif x < b:
                b = x
        return a, b


if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1]
    print sol.smallest_numbers(nums)

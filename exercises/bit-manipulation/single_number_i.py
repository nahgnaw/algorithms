# -*- coding: utf-8 -*-

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber2(self, nums):
        result = 0
        for x in nums:
            result ^= x
        return result

    def singleNumber3(self, nums):
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1
            
        for x in counts:
            if counts[x] == 1:
                return x

    def singleNumber4(self, nums):
        return 2 * sum(set(nums)) - sum(nums)




if __name__ == '__main__':
    nums = [0,1,3,4,0,4,3]
    sol = Solution()
    print sol.singleNumber(nums)
    print sol.singleNumber2(nums)

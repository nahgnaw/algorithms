# -*- coding: utf-8 -*-

"""
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example:
Given [1,2,4], return 1.
"""


class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, nums):
        import math

        if nums is None or len(nums) < 1:
            return 0

        sorted_nums = sorted(nums)

        perm_index = 1
        for i in xrange(len(nums)):
            rank = sorted_nums.index(nums[i])
            if i > 0:
                for j in xrange(0, i):
                    if nums[j] < nums[i]:
                        rank -= 1
            perm_index += rank * math.factorial(len(nums) - 1 - i)

        return perm_index

    def permutationIndex2(self, nums):
        import math

        if nums is None or len(nums) < 1:
            return 0

        perm_index = 1
        for i in xrange(len(nums)):
            rank = 0
            for j in xrange(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    rank += 1
            perm_index += rank * math.factorial(len(nums) - 1 - i)

        return perm_index

if __name__ == '__main__':
    nums = [4,1,2,3]
    sol = Solution()
    print sol.permutationIndex(nums)
    print sol.permutationIndex2(nums)

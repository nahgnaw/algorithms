# -*- coding: utf-8 -*-

"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        prev = lower
        for cur in [lower - 1] + nums + [upper + 1]:
            if cur - prev > 1:
                result.append(str(prev + 1) if cur - prev == 2 else str(prev + 1) + '->' + str(cur - 1))
            prev = cur
        return result

if __name__ == '__main__':
    nums = [0, 1, 3, 50, 75]
    lower, upper = 0, 99
    sol = Solution()
    print sol.findMissingRanges(nums, lower, upper)

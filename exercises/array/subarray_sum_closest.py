# -*- coding -*- 

"""
Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]

Challenge
O(nlogn) time
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    # O(nlogn)
    def subarraySumClosest(self, nums):
        sum_list = [[0, 0] for _ in xrange(len(nums) + 1)]
        for i in xrange(len(nums)):
            sum_list[i + 1] = [sum_list[i][0] + nums[i], i + 1]

        sum_list = sorted(sum_list, key=lambda x: x[0])

        min_diff = float('inf')
        index_pair = [0, 0]
        for i in xrange(1, len(sum_list)):
            diff = abs(sum_list[i][0] - sum_list[i-1][0])
            if diff < min_diff:
                min_diff = diff
                index_pair = [sum_list[i-1][1], sum_list[i][1]]

        return [min(index_pair), max(index_pair)-1]


if __name__ == '__main__':
    nums = [-3, 1, 1, -3, 5]
    sol = Solution()
    print sol.subarraySumClosest(nums)
# -*- coding: utf-8 -*-

"""
Given an array containing only 0s and 1s, find the length of the largest subarray which contains equal number of 0s and 1s. 

Expected time complexity is O(n).

Examples:

Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 6

Input: arr[] = {1, 1, 1, 1}
Output: 0

Input: arr[] = {0, 0, 1, 1, 0}
Output: 4
"""


class Solution(object):
    def largest_subarray(self, arr):
        if len(arr) < 2:
            return -1

        # sum_map stores the cumulative sum of all elements before arr[i].
        # key: the cumulative sum
        # value: the index i
        sum_map = {0: -1}
        cur_sum = 0
        max_len = 0

        for i in xrange(len(arr)):
            cur_sum += 1 if arr[i] == 1 else -1
            if cur_sum not in sum_map:
                sum_map[cur_sum] = i
            else:
                max_len = max(max_len, i - sum_map[cur_sum])
        return max_len


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 1, 1, 1]
    print sol.largest_subarray(arr)

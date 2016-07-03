# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
    # O(n^2)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_len = 1
        # dp[i]: length of longest increasing subsequence at i
        dp = [1] * len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len

    # O(nlogn)
    def lengthOfLIS2(self, nums):
        seq_size = 0
        # smallest_tail[i]: the smallest tail element among increasing subsequences of size i+1
        smallest_tail = [0] * len(nums)
        for n in nums:
            # if n is greater than all elements in smallest_tail, append n to smallest_tail, seq_size += 1
            # if smallest_tail[i-1] < n <= smallest_tail[i], update smallest_tail[i] with n, keep seq_size unchanged
            # since smallest_tail is sorted, binary search can be used
            left, right = 0, seq_size
            while not left == right:
                mid = (left + right) / 2
                if n > smallest_tail[mid]:
                    left = mid + 1
                else:
                    right = mid
            smallest_tail[left] = n
            seq_size = max(left + 1, seq_size)
        return seq_size



if __name__ == '__main__':
    nums = [10,9,2,5,1,2,5]
    sol = Solution()
    print sol.lengthOfLIS(nums)
    print sol.lengthOfLIS2(nums)
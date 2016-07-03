# -*- coding: utf-8 -*-

"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""


class Solution(object):
    # O(n^2)
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
            
        sorted_envelopes = sorted(envelopes, key=lambda x: x[0])
        # dp[i]: max number of Runssian Doll envelopes at index i in sorted_envelopes
        dp = [1] * len(envelopes)   # At least every envelope itself is a Russian Doll envelope
        max_number = 1
        for i in xrange(1, len(envelopes)):
            for j in xrange(i):
                if sorted_envelopes[j][0] < sorted_envelopes[i][0] and \
                   sorted_envelopes[j][1] < sorted_envelopes[i][1]:
                       dp[i] = max(dp[j] + 1, dp[i])
            max_number = max(max_number, dp[i])
        return max_number

    # O(nlogn)
    def maxEnvelopes2(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
          
        # First sort envelopes by width (ascending) and then by height (descending)
        sorted_envelopes = sorted(envelopes, key=lambda x: x[1], reverse=True)
        sorted_envelopes = sorted(sorted_envelopes, key=lambda x: x[0])
        
        # Extract heights in sorted_envelopes
        heights = [e[1] for e in sorted_envelopes]
        
        # Now the problem is equivalent to finding the length of the longest increasing sequence (LIS) in heights
        # smallest_tails[i]: the smallest tail element in all the increasing sequences with length i+1
        smallest_tails = [0] * len(heights)
        lis_len = 0
        for h in heights:
            # Use binary search to search for the insert index of h in smallest_tails
            # since smallest_tails is sorted
            left, right = 0, lis_len
            while left < right:
                mid = (left + right) / 2
                if h > smallest_tails[mid]:
                    left = mid + 1
                else:
                    right = mid
            # If h > smallest_tails[-1], left = lis_len, append h to smallest_tails
            # If smallest_tails[i-1] <= h < smallest_tails[i], left = i-1 (i>=1), update smallest_tails[i] with h
            smallest_tails[left] = h
            lis_len = max(lis_len, left + 1)
        return lis_len

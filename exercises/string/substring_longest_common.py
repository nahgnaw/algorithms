# -*- coding: utf-8 -*-

"""
Given two strings, find the longest common substring.

Return the length of it.

Example
Given A = "ABCD", B = "CBCE", return 2.

Note
The characters in substring should occur continuously in original string. This is different with subsequence.

Challenge
O(n x m) time and memory.
"""


class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    # O(mn*lcs)
    def longestCommonSubstring(self, A, B):
        if 0 in [len(A), len(B)]:
            return 0

        max_lcs_len = 0
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                walk = 0
                while i + walk < len(A) and j + walk < len(B) and A[i+walk] == B[j+walk]:
                    walk += 1
                max_lcs_len = max(max_lcs_len, walk)

        return max_lcs_len


if __name__ == '__main__':
    A = 'ABCD'
    B = 'BCD'
    sol = Solution()
    print sol.longestCommonSubstring(A, B)

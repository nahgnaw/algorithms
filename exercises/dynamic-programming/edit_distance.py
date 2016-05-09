# -*- coding: utf-8 -*-

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


class Solution(object):
    # Space: O(mn)
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]: the minumum number of steps required to convert word1[:i] to word2[:j]
        dp = [[0 for _ in xrange(len(word2) + 1)] for _ in xrange(len(word1) + 1)]
        # Initialization.
        for i in xrange(len(word1) + 1):
            dp[i][0] = i
        for j in xrange(len(word2) + 1):
            dp[0][j] = j
        
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[-1][-1]

    # Space: O(2n)
    def minDistance2(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        if not len1 or not len2:
            return max(len1, len2)
            
        if len1 < len2:
            self.minDistance(word2, word1)

        prev = range(len2 + 1)

        for i in xrange(1, len1 + 1):
            cur = [i] * (len2 + 1)
            for j in xrange(1, len2 + 1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = min(cur[j-1], prev[j-1], prev[j]) + 1
            prev = cur[:]
        return prev[-1]


    # Space: O(n)
    def minDistance3(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        if not len1 or not len2:
            return max(len1, len2)
            
        if len1 < len2:
            self.minDistance(word2, word1)

        dp = range(len2 + 1)

        for i in xrange(1, len1 + 1):
            left = i
            for j in xrange(1, len2 + 1):
                top_left = dp[j-1]
                top = dp[j]
                if word1[i-1] == word2[j-1]:
                    cur = top_left
                else:
                    cur = min(left, top_left, top) + 1
                dp[j-1] = left
                left = cur
            dp[-1] = left
        return dp[-1]

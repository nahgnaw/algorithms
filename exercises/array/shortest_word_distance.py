# -*- coding: utf-8 -*-

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length = len(words)
        ind_1, ind_2 = length, -length
        min_distance = length
        for i in xrange(length):
            if word1 == words[i]:
                ind_1 = i
            elif word2 == words[i]:
                ind_2 = i
            min_distance = min(min_distance, abs(ind_1 - ind_2))
        return min_distance
        
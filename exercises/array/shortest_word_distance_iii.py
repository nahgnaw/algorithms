# -*- coding: utf-8 -*-

"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
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
            if word2 == words[i]:
                if word1 == word2:
                    ind_1 = ind_2
                ind_2 = i
            min_distance = min(min_distance, abs(ind_1 - ind_2))
        return min_distance

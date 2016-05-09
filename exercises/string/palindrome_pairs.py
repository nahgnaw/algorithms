# -*- coding: utf-8 -*-

"""
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_map = {w: i for i, w in enumerate(words)}
        pairs = []
        for i, w in enumerate(words):
            for j in xrange(len(w) + 1):
                a, b = w[:j], w[j:]
                # b[::-1] + a + b is a palindrome.
                if a == a[::-1]:
                    b_ind = word_map.get(b[::-1], -1)
                    if b_ind not in [-1, i]:
                        pairs.append((b_ind, i))
                # a + b + a[::-1] is a palindorme.
                if b == b[::-1]:
                    a_ind = word_map.get(a[::-1], -1)
                    if a_ind not in [-1, i]:
                        pairs.append((i, a_ind))
        return list(set(pairs))

# -*- coding: utf-8 -*-

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = [0] * len(words)
        result = 0
        for i in xrange(len(words)):
            for c in words[i]:
                masks[i] |= 1 << ord(c) - ord('a')
            for j in xrange(i): 
                if not masks[i] & masks[j]:
                    result = max(result, len(words[i]) * len(words[j]))
        return result
# -*- coding: utf-8 -*-

"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                       for j in range(i+1, len(s)+1)
                       if s[i:j] in wordDict
                       for tail in dfs(j)]
            return memo[i]
                    
            
        memo = {len(s): ['']}
        return dfs(0)
        
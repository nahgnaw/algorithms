# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
            
        if len(strs) == 1:
            return strs[0]
            
        for i in xrange(len(strs[0])):
            ch = strs[0][i]
            for j in xrange(1, len(strs)):
                # One of the strings is exhausted
                if i == len(strs[j]):
                    return strs[0][:i]
                # Prefix ends
                if not ch == strs[j][i]:
                    return strs[0][:i]
                
        return strs[0]
    
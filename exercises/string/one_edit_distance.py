# -*- coding: utf-8 -*-

"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
            
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
            
        if len(t) - len(s) > 1:
            return False
        
        i = 0
        while i < len(s):
            if not s[i] == t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
            i += 1
        return len(t) - i == 1
        
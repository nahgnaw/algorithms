# -*- coding: utf-8 -*-

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        end = len(s) - 1
        last_word_len = 0
        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == ' ':    
                if last_word_len:
                    break
            else:
                last_word_len += 1
        return last_word_len
# -*- coding: utf-8 -*-

"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
            
        result = list(s)
        left, right = 0, len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return ''.join(result)
        
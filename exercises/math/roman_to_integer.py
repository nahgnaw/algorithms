# -*- coding: utf-8 -*-

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = roman_int_map[s[-1]]
        pivot = result
        for i in xrange(len(s) - 2, -1, -1):
            cur = roman_int_map[s[i]]
            if pivot <= cur:
                result += cur
            else:
                result -= cur
            pivot = cur
        return result
            
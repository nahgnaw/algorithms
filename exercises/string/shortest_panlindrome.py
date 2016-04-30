# -*- coding: utf-8 -*-

"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        for right in xrange(len(s) - 1, -1, -1):
            if s[left] == s[right]:
                left += 1

        if left == len(s):
            return s

        suffix = s[left:]
        return suffix[::-1] + self.shortestPalindrome(s[:left]) + suffix
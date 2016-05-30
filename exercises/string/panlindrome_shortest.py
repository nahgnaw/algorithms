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
        # Need recur on s[:left] since it is not necessarily a palindrome. 
        # E.g. abca
        return suffix[::-1] + self.shortestPalindrome(s[:left]) + suffix


    def shortestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Expand if characters on both sides are the same.
        # When the left end of s is reached, the solution if found.
        def expand(left, right):
            step = 1
            while left - step >= 0 and right + step < len(s):
                if not s[left-step] == s[right+step]:
                    break
                step += 1
            # If the left end of s is not reached, there is no solution yet.
            if left - step >= 0:
                return None
            return s[right+step:][::-1] + s
            
            
        if len(s) < 2:
            return s
            
        res = ''
        # Start expanding from the middle of s.
        mid = (len(s) - 1) / 2
        for i in xrange(mid, -1, -1):
            # The axis of symmetry can be two characters.
            if s[i] == s[i+1]:
                res = expand(i, i + 1)
                if res:
                    return res
            # The axis of symmetry can also be one character.
            res = expand(i, i)
            if res:
                return res
        return res
        
# -*- coding: utf-8 -*-

"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # matching[i][j]: if p[:i] matches s[:j].
        matching = [[False for _ in xrange(len(s) + 1)] for _ in xrange(len(p) + 1)]

        # An empty pattern matches an empty string.
        matching[0][0] = True

        # An empty pattern doesn't match any string.
        # for i in xrange(1, len(s) + 1):
        #     matching[0][i] = False

        # Empty s.
        for i in xrange(1, len(p) + 1):
            # matching[1][0] is False since a single character pattern won't match an empty string.
            matching[i][0] = i > 1 and p[i-1] == '*' and matching[i-2][0]

        for i in xrange(1, len(p) + 1):
            for j in xrange(1, len(s) + 1):
                if not p[i-1] == '*':
                    matching[i][j] = matching[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
                    matching[i][j] = matching[i-1][j] or matching[i-2][j]
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        matching[i][j] = matching[i][j] or matching[i][j-1]

        return matching[-1][-1]
        
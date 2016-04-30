# -*- coding: utf-8 -*-

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False

        ms = {}
        mt = {}
        for chs, cht in zip(s, t):
            if chs not in ms and cht not in mt:
                ms[chs] = cht
                mt[cht] = chs
            else:
                if not ms.get(chs) == cht or not mt.get(cht) == chs:
                    return False
        return True


if __name__ == '__main__':
    s, t = "ad", "dd"
    solution = Solution()
    print solution.isIsomorphic(s, t)

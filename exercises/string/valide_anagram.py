# -*- coding: utf-8 -*-

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    # O(n)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False
            
        mapping = {}
        for i in xrange(len(s)):
            mapping[s[i]] = mapping.setdefault(s[i], 0) + 1
            mapping[t[i]] = mapping.setdefault(t[i], 0) - 1
            
        for key in mapping:
            if not mapping[key] == 0:
                return False
        return True

    # O(nlogn)
    def isAnagram2(self, s, t):
        if not len(s) == len(t):
            return False
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = 'asdf'
    t = 'dfsa'
    sol = Solution()
    print sol.isAnagram(s, t)
    print sol.isAnagram2(s, t)

# -*- coding: utf-8 -*-


"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if len(d) <= 2:
                d[s[right]] = right
                right += 1
            if len(d) > 2:
                leftmost = min(d.values())
                del d[s[leftmost]]
                left = leftmost + 1
            max_len = max(max_len, right - left)
        return max_len



if __name__ == '__main__':
    s = 'eceba'
    sol = Solution()
    print sol.lengthOfLongestSubstringTwoDistinct(s)

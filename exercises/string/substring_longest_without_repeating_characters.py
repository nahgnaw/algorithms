# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = -1  # The index of the last seen character
        d = {}  # key: character, value: index
        for i, char in enumerate(s):
            # If char has been seen before, update start only if
            # the position of its last occurence is after start.
            if char in d and start < d[char]:
                start = d[char]
            d[char] = i # Update char's most recent index.
            max_len = max(max_len, i - start)
        return max_len


if __name__ == '__main__':
    s = 'abccccdefg'
    sol = Solution()
    print sol.lengthOfLongestSubstring(s)

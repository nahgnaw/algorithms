# -*- coding: utf-8 -*-

"""
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
Challenge
Rotate in-place with O(1) extra memory.
"""


class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        n = len(s)
        offset %= n
        left, right = s[:n-offset], s[n-offset:]
        s = left[::-1] + right[::-1]
        s = s[::-1]
        return s


if __name__ == '__main__':
    s = 'abcdefg'
    offset = 5
    sol = Solution()
    print sol.rotateString(s, offset)

# -*- coding: utf-8 -*-

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
            
        result = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if i >= len(s):
                break
            j = i + 1
            while j < len(s) and not s[j] == ' ':
                j += 1
            result.append(s[i:j])
            i = j
        return ' '.join(result[::-1])
        

if __name__ == '__main__':
    s = "the sky is blue"
    sol = Solution()
    print sol.reverseWords(s)

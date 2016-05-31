# -*- coding: utf-8 -*-

"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def _reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        if not s:
            return
        
        # Reverse each individual word.
        word_len = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                _reverse(i - word_len, i - 1)
                word_len = 0
            elif i == len(s) - 1:
                _reverse(i - word_len, i)
            else:
                word_len += 1
        
        # Reverse the entire string.   
        _reverse(0, len(s) - 1)



if __name__ == '__main__':
    s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
    sol = Solution()
    sol.reverseWords(s)
    print s

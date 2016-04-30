# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        walk = 0
        while walk < len(s):
            if s[walk] in parentheses.values():
                stack.append(s[walk])
            else:
                if not stack or not parentheses[s[walk]] == stack.pop():
                   return False
            walk += 1

        return len(stack) == 0
        

if __name__ == '__main__':
    s = ']](('
    sol = Solution()
    print sol.isValid(s)

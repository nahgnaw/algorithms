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
            return True
            
        parenthesis_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
            
        stack = []
        for c in s:
            if c in parenthesis_map.values():
                stack.append(c)
            else:
                if not stack or not parenthesis_map[c] == stack.pop():
                    return False
        return len(stack) == 0
        

if __name__ == '__main__':
    s = ']](('
    sol = Solution()
    print sol.isValid(s)

# -*- coding: utf-8 -*-

"""
Return a string's length using recursion. Don't use the built-in len() function.
"""


class Solution(object):
    def str_len(self, s):
        if s == '':
            return 0

        return self.str_len(s[1:]) + 1


if __name__ == '__main__':
    sol = Solution()
    s = 'asdfeadsf'
    print sol.str_len(s)

# -*- coding: utf-8 -*-

"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        # There can only be one bit that is one.
        return (n & (n - 1)) == 0


if __name__ == '__main__':
    sol = Solution()
    n = 1
    print sol.isPowerOfTwo(n)
    
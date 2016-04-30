# -*- coding: utf-8 -*-

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution(object):
    # Recursion
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        return False

    def isPowerOfThree2(self, n):
        if n > 1:
            while n % 3 == 0:
                n /= 3
        return n == 1

    def isPowerOfThree3(self, n):
        return n > 0 and 3 ** 19 % n == 0

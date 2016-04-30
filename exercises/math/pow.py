# -*- coding: utf-8 -*-

"""
Implement pow(x, n).
"""


class Solution(object):
    # Recursive
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    # iterative
    def myPow2(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        power = 1
        while n:
            if n & 1:   # n is odd
                power *= x
            x *= x
            n >>= 1
        return power
        
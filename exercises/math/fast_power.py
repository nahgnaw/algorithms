# -*- coding: utf-8 -*-

"""
Calculate the a^n % b where a, b and n are all 32bit integers.

Example
For 2^31 % 3 = 2

For 100^1000 % 1000 = 0

Challenge
O(logn)
"""


class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        elif n == 0:
            return 1 % b
        elif n < 0:
            return -1

        # (a * b) % p = ((a % p) * (b % p)) % p
        result = self.fastPower(a, b, n / 2)
        result = (result * result) % b
        if n % 2 == 1:
            result = (result * a) % b

        return result

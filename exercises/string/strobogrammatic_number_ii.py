# -*- coding: utf-8 -*-

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
"""


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = [''] if not n % 2 else n % 2 * list('018')
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
        return nums

    # Recursion
    def findStrobogrammatic2(self, n):
        odd_mid = ['8', '1', '0']
        even_mid = ['96', '88', '69', '11', '00']

        if n == 0:
            return ['']
        if n == 1:
            return odd_mid
        if n == 2:
            return even_mid[:-1]

        if n % 2:
            prev, mid = self.findStrobogrammatic2(n - 1), odd_mid
        else:
            prev, mid = self.findStrobogrammatic2(n - 2), even_mid

        return [num[:(n-1)/2] + m + num[(n-1)/2:] for num in prev for m in mid]
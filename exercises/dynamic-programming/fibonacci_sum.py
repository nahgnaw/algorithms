# -*- coding: utf-8 -*-

"""
Return the sum of n fibonacci numbers.
"""


class Solution(object):
    def fib_sum(self, n):
        if n < 1:
            return 0

        a = b = 1
        total = a
        for _ in xrange(n-1):
            total += b
            a, b = b, a + b
        return total


if __name__ == '__main__':
    sol = Solution()
    n = 5
    print sol.fib_sum(n)

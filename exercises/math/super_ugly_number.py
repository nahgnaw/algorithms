# -*- coding: utf-8 -*-

"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_numbers = [1]
        factor_indecies = [0] * len(primes)
        while n > 1:
            factors = [primes[i] * ugly_numbers[factor_indecies[i]] for i in xrange(len(primes))]
            next_ugly = min(factors)

            for i in xrange(len(factors)):
                if next_ugly == factors[i]:
                    factor_indecies[i] += 1

            ugly_numbers.append(next_ugly)
            n -= 1
        return ugly_numbers[-1]


if __name__ == '__main__':
    n = 10
    primes = [2, 3, 5]
    sol = Solution()
    print sol.nthSuperUglyNumber(n, primes)

# -*- coding: utf-8 -*-

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""

class Solution(object):
    # Using heap
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from heapq import *

        heap = []
        uglies = [1]
        for _ in xrange(1, n):
            ugly = uglies[-1]
            for x in [2, 3, 5]:
                heappush(heap, ugly * x)
            next_ugly = heappop(heap)
            while len(heap) and heap[0] == next_ugly:
                heappop(heap)
            uglies.append(next_ugly)
        return uglies[-1]

    # Dynamic programming
    def nthUglyNumber2(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        for _ in xrange(1, n):
            f2, f3, f5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            min_f = min(f2, f3, f5)
            if min_f == f2:
                i2 += 1
            if min_f == f3:
                i3 += 1
            if min_f == f5:
                i5 += 1
            ugly.append(min_f)
        return ugly[-1]


if __name__ == '__main__':
    n = 10
    sol = Solution()
    print sol.nthUglyNumber2(n)
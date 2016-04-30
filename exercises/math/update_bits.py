# -*- coding: utf-8 -*-

"""
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N located at i and starting at j)

Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2

Note
In the function, the numbers N and M will given in decimal, you should also return a decimal number.

Challenge
Minimum number of operations?

Clarification
You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.
"""


class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        mask = 0
        ones = ~0
        if j < 31:
            left = ones << (j + 1)
            right = (1 << i) - 1
            mask = left | right
        else:
            mask = (1 << i) - 1
        result = (n & mask) | (m << i)

        if result >= 2 ** 31:
            result -= 2 ** 32

        return result


if __name__ == '__main__':
    n, m, i, j = 456,31,27,31
    sol = Solution()
    print sol.updateBits(n, m, i, j)

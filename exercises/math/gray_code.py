# -*- coding: utf-8 -*-

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        i=0: 0
        i=1: 0(0), 1(1)
        i=2: 0(00), 1(01), 3(11), 2(10)
        i=3: 0(000), 1(001), 3(011), 2(010), 6(110), 7(111), 5(101), 4(100)
        ...
        """
        result = [0]
        for i in xrange(n):
            result += [2 ** i + x for x in result[::-1]]
        return result

# -*- coding: utf-8 -*-

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
            
        if num in [1, 2, 3, 5]:
            return True

        for x in [2, 3, 5]:
            if num % x:
                continue
            else:
                num /= x
                return self.isUgly(num)

        return False

    def isUgly2(self, num):
        if num == 0:
            return False

        for x in [2, 3, 5]:
            while not num % x:
                num /= x
        return num == 1


if __name__ == '__main__':
    num = 2
    sol = Solution()
    print sol.isUgly2(num)

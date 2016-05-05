# -*- coding: utf-8 -*-

"""
Increase 1 to the given number represented by an array. 
"""


class Solution(object):
    def increment(self, num):
        if not num:
            return 1

        carry = 1
        for i in xrange(len(num) - 1, -1, -1):
            sum = num[i] + carry
            carry = sum / 10
            num[i] = sum % 10
        if carry:
            num = [1] + num
        return num


if __name__ == '__main__':
    sol = Solution()
    num = [3, 0, 9]
    print sol.increment(num)

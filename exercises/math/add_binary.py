# -*- coding: utf-8 -*-

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            result.append(str(sum % 2))
            carry = sum / 2
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])


if __name__ == '__main__':
    a, b = '11', '1'
    sol = Solution()
    print sol.addBinary(a, b)

# -*- coding: utf-8 -*-

"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        
        for i1, e1 in enumerate(reversed(num1)):
            for i2, e2 in enumerate(reversed(num2)):
                result[i1+i2] += int(e1) * int(e2)
                result[i1+i2+1] += result[i1+i2] / 10   # carry
                result[i1+i2] %= 10
        
        # Remove zeros in the front
        while len(result) > 1 and not result[-1]:
            result.pop()
                
        return ''.join(map(str, result[::-1]))
                
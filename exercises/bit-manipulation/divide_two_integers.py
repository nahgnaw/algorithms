# -*- coding: utf-8 -*-

"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
            
        positive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                temp <<= 1
                i <<= 1
                
        if not positive:
            result = -result
        return result
            
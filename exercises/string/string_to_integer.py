# -*- coding: utf-8 -*-

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        
        result = 0
        
        # Remove leading whitespaces.
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
                
        # Deal with signs.
        sign = 1
        if not str[i].isdigit():
            if str[i] == '+':
                sign = 1
            elif str[i] == '-':
                sign = -1
            else:
                return 0
            i += 1
                
        # Collect numerical digits.
        while i < len(str) and str[i].isdigit():
            result = 10 * result + int(str[i])
            i += 1
        result *= sign
            
        # Check overflow.
        return min(2 ** 31 - 1, result) if result >= 0 else max(-2 ** 31, result)
            

if __name__ == '__main__':
    str = '-+1'
    sol = Solution()
    print sol.myAtoi(str)

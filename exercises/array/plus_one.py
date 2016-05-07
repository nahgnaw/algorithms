# -*- coding: utf-8 -*-

"""
Increase 1 to the given number represented by an array. 
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return 1

        carry = 1
        for i in xrange(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            carry = sum / 10
            digits[i] = sum % 10
        if carry:
            digits = [1] + digits
        return digits
        
        
if __name__ == '__main__':
    sol = Solution()
    num = [3, 0, 9]
    print sol.increment(num)

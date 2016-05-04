# -*- coding: utf-8 -*-

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
            
        if x in [0, 1]:
            return x
        
        left, right = 1, x
        sqrt = left
        while left <= right:
            mid = (left + right) / 2
            s = mid * mid
            if s == x:
                return mid
            elif s < x:
                left = mid + 1
                sqrt = mid
            else:
                right = mid - 1
        return sqrt


    # Float version
    def myFloatSqrt(self, x, precision):

        def helper(left, right):
            while left < right:
                mid = (left + right) / 2
                s = mid * mid
                if abs(s - x) < precision:
                    return mid
                elif s < x:
                    left = mid
                else:
                    right = mid
            # return left

        x = float(x)
        if x in [0.0, 1.0]:
            return x

        if x > 1:
            return helper(1.0, x)
        else:
            return helper(x, 1.0)


if __name__ == '__main__':
    sol = Solution()
    x = 0.000067876
    precision = 0.001
    print sol.myFloatSqrt(x, precision)

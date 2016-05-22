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

    # Float version. Newton's method.
    # Update rule: x_new = x_old - f(x_old) / f'(x_old)
    # Here, f(x_old) = x_old^2 - x, f'(x_old) = 2 * x_old
    def myFloatSqrt2(self, x, precision):
        x = float(x)
        sqrt = 1.0
        while True:
            sqrt_new = sqrt - (sqrt ** 2 - x) / (2 * sqrt)
            if abs(sqrt_new - sqrt) <= precision:
                break
            sqrt = sqrt_new
        return sqrt_new


if __name__ == '__main__':
    sol = Solution()
    x = 0.000098
    precision = 0.000001
    print sol.myFloatSqrt(x, precision)
    print sol.myFloatSqrt2(x, precision)

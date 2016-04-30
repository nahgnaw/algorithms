# -*- coding: utf-8 -*-

"""
Implement multiplication and division using bit operations.
"""


class Solution(object):

    def multiply(self, x, y):
        if 0 in [x, y]:
            return 0

        if y < 0:
            x = -x
            y = -y

        result = 0
        # Decompose y into two's powers
        while y:
            if y & 1:
                result += x
            x <<= 1
            y >>= 1
        return result

    def divide(self, x, y):
        if not y:
            return None

        if not x:
            return 0

        result, sign = 0, 1

        if x < 0:
            x = -x
            sign ^= 1
        if y < 0:
            y = -y
            sign ^= 1

        while x >= y:
            x -= y
            result += 1

        return result if sign else -result


if __name__ == '__main__':
    sol = Solution()
    x, y = 38, -3
    print sol.multiply(x, y)
    print sol.divide(x, y)


# -*- coding: utf-8 -*-

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        number, operator = 0, '+'
        stack = []
        for i, c in enumerate(s):
            if c.isdigit():
                number = 10 * number + int(c)
            if c in ['+', '-', '*', '/'] or i == len(s) - 1:
                if operator == '+':
                    stack.append(number)
                elif operator == '-':
                    stack.append(-number)
                elif operator == '*':
                    stack.append(stack.pop() * number)
                elif operator == '/':
                    tmp = stack.pop()
                    if tmp / number < 0 and tmp % number:
                        stack.append(tmp / number + 1)
                    else:
                        stack.append(tmp / number)
                operator = c
                number = 0
        return sum(stack)

    def calculate2(self, s):
        cur_res, result = 0, 0
        op = '+'
        i = 0
        while i < len(s):
            if s[i].isdigit():
                number = int(s[i])
                while i + 1 < len(s) and s[i+1].isdigit():
                    number = 10 * number + int(s[i+1])
                    i += 1
                if op == '+':
                    cur_res += number
                elif op == '-':
                    cur_res -= number
                elif op == '*':
                    cur_res *= number
                elif op == '/':
                    if cur_res < 0 and cur_res % number:
                        cur_res = cur_res / number + 1
                    else:
                        cur_res /= number
            elif s[i] in ['+', '-', '*', '/']:
                if s[i] in ['+', '-']:
                    result += cur_res
                    cur_res = 0
                op = s[i]
            i += 1
        return result + cur_res


if __name__ == '__main__':
    s = '14 - 3 / 2'
    sol = Solution()
    print sol.calculate2(s)

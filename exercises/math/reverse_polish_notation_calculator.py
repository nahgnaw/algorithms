# -*- coding: utf-8 -*-

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b + 1 if a * b < 0 and a % b else a / b
        }

        if len(tokens) < 2:
            return int(tokens[0])

        stack = []
        for ch in tokens:
            if not ch or ch == ' ':
                continue

            if ch in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operations[ch](op1, op2))
            else:
                stack.append(int(ch))

        return stack[-1]

if __name__ == '__main__':
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print sol.calculate(tokens)

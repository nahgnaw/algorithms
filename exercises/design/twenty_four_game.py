# -*- coding: utf-8 -*-

"""
Twenty-four game: use four numbers and operators (+, -, *, /) to produce 24.
"""


class TwentyFourGame(object):

    operators = '+-*/'
    target = 24
    threshold = 0.0001

    class Result(object):
        def __init__(self, num, exp):
            self.number = num
            self.expression = exp

    def solve(self, numbers):

        def dfs():
            if len(operands) == 1 and abs(operands[0].number - self.target) < self.threshold:
                results.append(operands[0].expression)
                return

            operand_size = len(operands)
            for i in xrange(operand_size):
                num1 = operands[i]
                operands.pop(i)
                for j in xrange(i, operand_size - 1):
                    num2 = operands[j]
                    operands.pop(j)
                    tmp1, tmp2 = 0, 0
                    for operator in self.operators:
                        symmetric = False
                        if operator == '+':
                            tmp1 = float(num1.number) + num2.number
                            symmetric = True
                        elif operator == '-':
                            tmp1 = float(num1.number) - num2.number
                            tmp2 = float(num2.number) - num1.number
                        elif operator == '*':
                            tmp1 = float(num1.number) * num2.number
                            symmetric = True
                        elif operator == '/':
                            try:
                                tmp1 = float(num1.number) / num2.number
                                tmp2 = float(num2.number) / num1.number
                            except ZeroDivisionError:
                                continue

                        operands.append(self.Result(tmp1, '({}{}{})'.format(num1.expression, operator, num2.expression)))
                        dfs()
                        operands.pop()

                        if not symmetric:
                            operands.append(self.Result(tmp2, '({}{}{})'.format(num2.expression, operator, num1.expression)))
                            dfs()
                            operands.pop()

                    operands.insert(j, num2)
                operands.insert(i, num1)

        operands = [self.Result(num, str(num)) for num in numbers]
        results = []
        dfs()
        return results

    


if __name__ == '__main__':
    game = TwentyFourGame()
    nums = [1,3,6,4]
    print game.solve(nums)

# -*- coding: utf-8 -*-

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""


class Solution(object):
    """
    Consider a graph which consists of number 0, 1,...,n as
    its nodes. Node j is connected to node i via an edge if  
    and only if either j = i + (a perfect square number) or 
    i = j + (a perfect square number). 
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1

        step = 0
        nodes = set([n])
        while nodes:
            step += 1
            temp = set()
            for node in nodes:
                for x in squares:
                    if node == x:
                        return step
                    elif node < x:
                        break
                    else:
                        temp.add(node - x)
            nodes = temp

        return step
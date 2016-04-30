# -*- coding: utf-8 -*-

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(pos):
            if pos == unfilled_count:
                return True
            
            x, y = unfilled[pos]
            for i in xrange(1, 10):
                if is_valid(str(i), x, y):
                    board[x][y] = str(i)
                    if dfs(pos + 1):
                        return True
                    board[x][y] = '.'
            return False
            
        def is_valid(num, x, y):
            for i in xrange(len(board)):
                # Check if num is already in the row
                if board[x][i] == num:
                    return False
                # Check if num is already in the column
                if board[i][y] == num:
                    return False
                # Check if num is already in the sub-box
                if board[x/3*3+i/3][y/3*3+i%3] == num:
                    return False
            return True
        
        unfilled = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    unfilled.append((i, j))
        unfilled_count = len(unfilled)
        
        dfs(0)

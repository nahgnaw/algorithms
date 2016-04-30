# -*- coding: utf-8 -*-

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def count_live_neighbors(i, j):
            return sum([board[x][y] & 1 for x, y in \
                [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), \
                (i+1, j+1), (i+1, j), (i+1, j-1), (i,j-1)] \
                    if 0 <= x < m and 0 <= y < n])
                  
        if not board or not board[0]:
            return
                    
        m, n = len(board), len(board[0])
        
        # For each cell, use two digits to represent the states.
        # The right digit represents the current state.
        # The left digit represents the next state.
        # 00: current dead, next dead
        # 01: current live, next dead
        # 10: current dead, next live
        # 11: current live, next live
        for i in xrange(m):
            for j in xrange(n):
                live_count = count_live_neighbors(i, j)
                current_state = board[i][j] & 1
                if current_state:
                    if 2 <= live_count <= 3:
                        board[i][j] = 3 # 3 means "11"
                else:
                    if live_count == 3:
                        board[i][j] = 2 # 2 means "10"
                        
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1   # Only keep the next state
        
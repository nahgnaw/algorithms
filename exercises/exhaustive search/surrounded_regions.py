# -*- coding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution(object):
    # DFS
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def flip(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or not board[x][y] == 'O':
                return
                
            board[x][y] = '*'
            flip(x-1, y)
            flip(x+1, y)
            flip(x, y+1)
            flip(x, y-1)
        
        if not board or not board[0]:
            return
        
        for i in [0, len(board)-1]:
            for j in xrange(len(board[0])):
                flip(i, j)
        for j in [0, len(board[0])-1]:
            for i in xrange(len(board)):
                flip(i, j)
                
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
             
    # BFS       
    def solve2(self, board):
    
        from collections import deque
        
        if not board or not board[0]:
            return
        
        q = deque([])
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (i in [0, len(board)-1] or j in [0, len(board[0])-1]) and board[i][j] == 'O':
                    q.append((i, j))
                        
        while q:
            x, y = q.popleft()
            board[x][y] = '*'
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                            q.append((i, j))
                
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

                    
if __name__ == '__main__':
    board = [['O', 'O', 'O'], ['O', 'O', 'O']]
    sol = Solution()
    sol.solve2(board)
    print board

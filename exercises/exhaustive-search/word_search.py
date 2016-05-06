# -*- coding: utf-8 -*-


"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, pos):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
                
            if visited[x][y]:
                return False
              
            if board[x][y] == word[pos]:
                if pos == len(word) - 1:
                    return True
                # Mark this char visited so later search won't be using it.
                visited[x][y] = True  
                up = dfs(x, y+1, pos+1)
                down = dfs(x, y-1, pos+1)
                left = dfs(x-1, y, pos+1)
                right = dfs(x+1, y, pos+1)
                # If there is no match, make this char available again.
                visited[x][y] = up or down or left or right
                return up or down or left or right
            
        visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'XCD'
    sol = Solution()
    print sol.exist(board, word)

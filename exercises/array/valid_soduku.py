# -*- coding: utf-8 -*-

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r_set = set()
        c_set = set()
        s_set = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if not board[i][j] == '.':
                    num = board[i][j]
                    if (i, num) in r_set or (j, num) in c_set or (i/3, j/3, num) in s_set:
                        return False
                    r_set.add((i, num))
                    c_set.add((j, num))
                    s_set.add((i/3, j/3, num))
        return True
        


if __name__ == '__main__':
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    sol = Solution()
    print sol.isValidSudoku(board)

# -*- coding: utf-8 -*-

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_valid(pos):
            for i in xrange(pos):
                # Two queens cannot be in the same row, the same column, or the same diagonal
                if queen_loc[i] == queen_loc[pos] or pos - i == abs(queen_loc[pos] - queen_loc[i]):
                    return False
            return True
            
        def print_solution():
            sol = [['.'] * n for _ in xrange(n)]
            for i in xrange(n):
                sol[i][queen_loc[i]] = 'Q'
                sol[i] = ''.join(sol[i])
            results.append(sol)
            
        def dfs(cur):
            if cur == n:
                print_solution()
                return
                
            for i in xrange(n):
                queen_loc[cur] = i
                if is_valid(cur):
                    dfs(cur + 1)
        
        if not n:
            return []
            
        results = []
        queen_loc = [-1] * n    # queen_loc[i] = j means there is a queen at (i, j)
        dfs(0)  # Start from the first queen
        return results


if __name__ == '__main__':
    n = 4
    sol = Solution()
    print sol.solveNQueens(n)
        
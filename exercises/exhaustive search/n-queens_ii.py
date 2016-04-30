# -*- coding: utf-8 -*-

"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_valid(pos):
            for i in xrange(pos):
                if queen_loc[i] == queen_loc[pos] or pos - i == abs(queen_loc[pos] - queen_loc[i]):
                    return False
            return True
            
        def dfs(cur):
            if cur == n:
                solution_count[0] += 1
                return
                
            for i in xrange(n):
                queen_loc[cur] = i
                if is_valid(cur):
                    dfs(cur + 1)
        
        if not n:
            return 0
            
        solution_count = [0]
        queen_loc = [-1] * n    # queen_loc[i] = j means there is a queen at (i, j)
        dfs(0)  # Start from the first queen
        return solution_count[0]
        
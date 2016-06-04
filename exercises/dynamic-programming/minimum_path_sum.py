# -*- coding: utf-8 -*-

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        sol = [[0 for j in xrange(n)] for i in xrange(m)]
        sol[0][0] = grid[0][0]

        for i in xrange(1, m):
            sol[i][0] = grid[i][0] + sol[i-1][0]
        for j in xrange(1, n):
            sol[0][j] = grid[0][j] + sol[0][j-1]

        for i in xrange(1, m):
            for j in xrange(1, n):
                sol[i][j] = grid[i][j] + min(sol[i-1][j], sol[i][j-1])

        return sol[-1][-1]

    def minPathSum2(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        sol = [0 for i in xrange(m)]
        sol[0] = grid[0][0]

        for i in xrange(1, m):
            sol[i] = grid[i][0] + sol[i-1]

        for j in xrange(1, n):
            sol[0] += grid[0][j]
            for i in xrange(1, m):
                sol[i] = grid[i][j] + min(sol[i], sol[i-1])
        return sol[-1]


if __name__ == '__main__':
    grid = [[1,2,3], [4,5,6], [7,8,9]]
    sol = Solution()
    print sol.minPathSum2(grid)

# -*- coding: utf-8 -*-

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


class Solution(object):
    # Space O(mn)
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        
        for i in xrange(m):
            if not obstacleGrid[i][0]:
                dp[i][0] = 1
            else:
                break
                
        for j in xrange(n):
            if not obstacleGrid[0][j]:
                dp[0][j] = 1
            else:
                break
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[-1][-1]
            
    # Space O(n)    
    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        sol = [0 for i in xrange(m)]

        for i in xrange(m):
            if not obstacleGrid[i][0]:
                sol[i] = 1
            else:
                break

        for j in xrange(1, n):
            if sol[0] and not obstacleGrid[0][j]:
                sol[0] = 1
            else:
                sol[0] = 0
            for i in xrange(1, m):
                if obstacleGrid[i][j]:
                    sol[i] = 0
                else:
                    sol[i] = sol[i] + sol[i-1]

        return sol[-1]

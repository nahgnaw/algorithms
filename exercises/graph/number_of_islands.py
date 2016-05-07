# -*- coding: utf-8 -*-

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    # Depth first search
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j , j+1, j-1))
                return 1
            return 0

        return sum(sink(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])))


    # BFS
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        
        # BFS sets all the elements in one island to '0'    
        def bfs(x, y):
            connections = deque([(x,y)])
            while connections:
                x0, y0 = connections.popleft()
                for x1, y1 in [(x0-1, y0), (x0+1, y0), (x0, y0-1), (x0, y0+1)]:
                    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] == '1':
                        grid[x1][y1] = '0'
                        connections.append((x1, y1))
            
        if not len(grid) or not len(grid[0]):
            return 0
        
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                # Count how many times the bfs() function was called.
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count
                    
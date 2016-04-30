# -*- coding: utf-8 -*-

"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from collections import deque

        m, n = len(rooms), len(rooms[0])
        # Push all gates to the queue
        queue = deque([(i, j) for i, row in enumerate(rooms) for j, cell in enumerate(row) if not cell])
        while queue:
            # BFS from a gate
            i, j = queue.popleft()
            for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ii < m and 0 <= jj < n and rooms[ii][jj] > 2 ** 30:
                    rooms[ii][jj] = rooms[i][j] + 1
                    # Push visited rooms to the queue
                    queue.append((ii, jj))
        

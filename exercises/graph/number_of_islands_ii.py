# -*- coding: utf-8 -*-

"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""


class Solution(object):
    # Union find.
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Find root of p with path compression.
        def find(p):
            if not p == parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        # Return the number of islands decreased by this union operation.
        def union(p, q):
            p, q = find(p), find(q)
            if p == q:
                # If p and q are already connected, don't decrease the number of islands.
                return 0
            # Only connect smaller trees to bigger trees.
            if rank[p] < rank[q]:
                parent[p] = q
            elif rank[p] > rank[q]:
                parent[q] = p
            else:
                parent[q] = p
                rank[p] += 1
            # Once two points are connected, decrease the number of islands by 1.
            return 1
        
        
        parent = {}
        rank = {}
        count = 0
        counts = []
        
        for x, y in positions:
            parent[(x, y)] = (x, y)
            rank[(x, y)] = 0
            count += 1
            
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (i,j) in parent:
                    count -= union((x,y), (i,j))
            counts.append(count)
        return counts

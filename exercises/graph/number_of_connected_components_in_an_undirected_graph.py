# -*- coding: utf-8 -*-

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class Solution(object):
    # DFS
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(x, visited, neighbors):
            if visited[x]:
                return

            visited[x] = 1
            for j in neighbors[x]:
                dfs(j, visited, neighbors)

        visited = [0] * n
        neighbors = {x: [] for x in xrange(n)}
        for s, t in edges:
            neighbors[s].append(t)
            neighbors[t].append(s)

        result = 0
        for i in xrange(n):
            if not visited[i]:
                dfs(i, visited, neighbors)
                result += 1

        return result

    # BFS
    def countComponents2(self, n, edges):
        neighbors = {x: [] for x in xrange(n)}
        for s, t in edges:
            neighbors[s].append(t)
            neighbors[t].append(s)
            
        result = 0
        for i in xrange(n):
            component = [i]
            result += 1 if i in neighbors else 0
            for j in component:
                component += neighbors[j]
                del neighbors[j]

        return result

    # Union find
    def countComponents3(self, n, edges):
        # Find root of p with path compression.
        def root(p):
            if not p == parent[p]:
                parent[p] = root(parent[p])
            return parent[p]
        
        # Return the number of connected components decreased by connecting x and y.
        def union(x, y):
            x, y = root(x), root(y)
            # If x and y are already connected (sharing the same root),
            # nothing needs to be done.
            if x == y:
                return 0
            # Only connect smaller trees to larger ones.
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                # Only increase the rank when x and y have the same rank.
                parent[y] = x
                rank[x] += 1
            return 1
        
        # First consider every node as an isolated node.
        parent = range(n)
        rank = [0] * n
        count = n
        
        # For every edge xy, connect x and y.
        for x, y in edges:
            count -= union(x, y)
        return count
        

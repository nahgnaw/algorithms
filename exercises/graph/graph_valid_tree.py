# -*- coding: utf-8 -*-

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class Solution(object):
    # Union find
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not len(edges) == n - 1:
            return False
            
        parent = range(n)
            
        def find(x):
            return x if parent[x] == x else find(parent[x])
            
        def union(e):
            x, y = map(find, e)
            parent[x] = y
            return not x == y
            
        return all(map(union, edges))

    # DFS
    def validTree(self, n, edges):
        if not len(edges) == n - 1:
            return False
            
        neighbors = {i: [] for i in xrange(n)}
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        
        def visit(x):
            map(visit, neighbors.pop(x, []))
            
        visit(0)
        return not neighbors
        

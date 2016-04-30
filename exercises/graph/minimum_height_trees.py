# -*- coding: utf-8 -*-

"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?
"""


class Solution(object):
    """
    Remove the leaves, update the degrees of inner vertexes. Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer.
    """
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        neighbors = [set() for _ in xrange(n)]
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)

        leaves = [i for i in xrange(n) if len(neighbors[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = neighbors[i].pop()
                neighbors[j].remove(i)
                if len(neighbors[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves

        return leaves
        
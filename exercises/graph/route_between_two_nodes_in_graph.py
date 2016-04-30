# -*- coding: utf-8 -*-

"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Example
Given graph:

A----->B----->C
 \     |
  \    |
   \   |
    \  v
     ->D----->E
for s = B and t = E, return true

for s = D and t = C, return false
"""


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    # DFS
    def hasRoute(self, graph, s, t):
        
        def dfs(v):
            if v == t:
                return True

            visited.append(v)
            for i in v.neighbors:
                if i in visited:
                    continue
                if dfs(i):
                    return True

            return False

        visited = []
        return dfs(s)

    # BFS
    def hasRoute2(self, graph, s, t):
        from collections import deque

        q = deque([s])
        visited = []
        while q:
            node = q.popleft()
            if node == t:
                return True
            visited.append(node)
            for i in node.neighbors:
                if i not in visited:
                    q.append(i)
        return False

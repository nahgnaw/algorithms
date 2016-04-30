# -*- coding: utf-8 -*-

"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Note
You can assume that there is at least one topological order in the graph.

Challenge
Can you do it in both BFS and DFS?
"""


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    # BFS
    def topSort(self, graph):
        if not graph:
            return []

        indegree = {node: 0 for node in graph}
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1
        
        start_nodes = [node for node in indegree if indegree[node] == 0]
        if not start_nodes:
            return []

        from collections import deque

        topo_order = []
        q = deque(start_nodes)
        while q:
            node = q.popleft()
            topo_order.append(node)
            for i in node.neighbors:
                indegree[i] -= 1
                if not indegree[i]:
                    q.append(i)
        return topo_order

    # DFS
    def topSort2(self, graph):
        def dfs(node):
            topo_order.append(node)
            for x in node.neighbors:
                indegree[x] -= 1
                if not indegree[x]:
                    dfs(x)

        if not graph:
            return []

        indegree = {node: 0 for node in graph}
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1
        
        start_nodes = [node for node in indegree if indegree[node] == 0]
        if not start_nodes:
            return []

        topo_order = []
        for node in start_nodes:
            dfs(node)
        return topo_order


if __name__ == '__main__':
    a = DirectedGraphNode(1)
    b = DirectedGraphNode(2)
    c = DirectedGraphNode(3)
    d = DirectedGraphNode(4)
    e = DirectedGraphNode(5)
    a.neighbors = [b, c]
    b.neighbors = [d, e]

    sol = Solution()
    print sol.topSort2([a,b,c,d,e])

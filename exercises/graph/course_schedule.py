# -*- coding: utf-8 -*-

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
"""


class Solution(object):
    # DFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Construct graph.
        neighbors = [[] for _ in xrange(numCourses)]
        for s, t in prerequisites:
            neighbors[s].append(t) # s has prerequisite t
        # Record if a vertex has been visited. "0" means a vertex hasn't been vistied.
        visited = [0 for _ in xrange(numCourses)]
        
        # Return False if a directed cycle is found. Return True otherwise.
        def dfs(v):
            # "-1" means v has been visited before, and thus a directed cycle is found.
            if visited[v] == -1:
                return False
            # "1" means there is no direct cycle on v and its successors.
            if visited[v] == 1:
                return True
            # Mark v as visited.
            visited[v] = -1
            # Recurse on the neighbors of v.
            for u in neighbors[v]:
                if not dfs(u):
                    return False
            # If no directed cycle is found, mark visited[v] as 1.
            visited[v] = 1
            return True
            
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

    # BFS
    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        
        # For each course, record the number of courses taking it as a prerequisite.
        indegrees = [0 for _ in xrange(numCourses)]
        
        # Construct graph.
        neighbors = [[] for _ in xrange(numCourses)]
        for s, t in prerequisites:
            neighbors[s].append(t)  # s has prerequisite t
            indegrees[t] += 1
        
        # Collect all the courses that are not prerequiste for any course.
        # These course should be taken at last.
        queue = deque()
        for i in xrange(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        count = numCourses  
        while queue:
            course = queue.popleft()
            for v in neighbors[course]:
                # "Remove" the edge between course and v
                indegrees[v] -= 1
                if not indegrees[v]:
                    # If v is no longer a prerequisite for other courses, put it in the queue.
                    # If there is no directed cycle, every vertex will end up in the queue.
                    queue.append(v)
            count -= 1
        return count == 0
        

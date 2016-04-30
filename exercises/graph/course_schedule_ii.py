# -*- coding: utf-8 -*-

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
"""


class Solution(object):
    # DFS
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
            # If no directed cycle is found, mark visited[v] as 1 and put v into the result.
            visited[v] = 1
            result.append(v)
            return True
        
        result = []
        for i in xrange(numCourses):
            if not dfs(i):
                return []
        return result

    # BFS
    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        
        # For each course, record the number of courses taking it as a prerequisite.
        indegrees = [0 for _ in xrange(numCourses)]
        
        # Construct graph.
        neighbors = [[] for _ in xrange(numCourses)]
        for s, t in prerequisites:
            neighbors[s].append(t)  # s has prerequisite t
            indegrees[t] += 1
        
        # Collect all the courses that are not prerequisites for any course.
        # These courses should be taken at last.
        queue = deque()
        for i in xrange(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        count = numCourses
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for v in neighbors[course]:
                # "Remove" the edge between course and v
                indegrees[v] -= 1
                if not indegrees[v]:
                    # If v is no longer a prerequisite for other courses, put it in the queue.
                    # If there is no directed cycle, every vertex will end up in the queue.
                    queue.append(v)
            count -= 1
            
        if count == 0:
            return result[::-1]
        else:
            return []

# -*- coding: utf-8 -*-

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    # Recursive
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def get_depth_sum(nested_list, depth):
            for x in nested_list:
                if x.isInteger():
                    result[0] += depth * x.getInteger()
                else:
                    get_depth_sum(x.getList(), depth + 1)
        
        if not nestedList:
            return 0
        
        result =[0]
        get_depth_sum(nestedList, 1)
        return result[0]

    # Iterative
    def depthSum2(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        from collections import deque
        
        if not nestedList:
            return 0
            
        q = deque()
        for x in nestedList:
            q.append((x, 1))
            
        result = 0
        while q:
            q_size = len(q)
            for _ in xrange(q_size):
                x, depth = q.popleft()
                if x.isInteger():
                    result += x.getInteger() * depth
                else:
                    for y in x.getList():
                        q.append((y, depth + 1))
        return result


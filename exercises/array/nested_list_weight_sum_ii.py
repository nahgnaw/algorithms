# -*- coding: utf-8 -*-

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
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
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        from collections import deque
        
        if not nestedList:
            return 0
            
        q = deque()
        for x in nestedList:
            q.append(x)
        
        # Gather integer sums by level
        integer_level_sum = []
        depth = 0
        while q:
            q_size = len(q)
            level_sum = 0
            for _ in xrange(q_size):
                x = q.popleft()
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        q.append(y)
            integer_level_sum.append(level_sum)
            depth += 1
        
        # Compute weight sum
        result = 0        
        for d in xrange(depth, 0, -1):
            result += d * integer_level_sum[depth - d]
        return result
        
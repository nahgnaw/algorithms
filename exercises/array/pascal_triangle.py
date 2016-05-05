# -*- coding: utf-8 -*-

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
            
        result = []
        for i in xrange(numRows):
            row = [1] * (i+1)
            if i > 1:
                for j in xrange(1, i):
                    row[j] = result[-1][j-1] + result[-1][j]
            result.append(row)
        return result
            
# -*- coding: utf-8 -*-

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    # O(n * n) memory
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        path_sum = []
        for row in triangle:
            path_sum.append(row[:])

        n = len(triangle)
        for i in xrange(n - 2, -1, -1):
            for j in xrange(0, i + 1):
                path_sum[i][j] = triangle[i][j] + min(path_sum[i+1][j], path_sum[i+1][j+1])

        return path_sum[0][0]

    # O(n) memory
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        path_sum = triangle[-1][:]

        n = len(triangle)
        for i in xrange(n - 2, -1, -1):
            for j in xrange(0, i + 1):
                path_sum[j] = triangle[i][j] + min(path_sum[j], path_sum[j+1])

        return path_sum[0]

    def minimumTotal3(self, triangle):
        def _dfs(x, y):
            if x == len(triangle):
                return 0

            if not d[x][y] == float('-inf'):
                return d[x][y]

            left, right = _dfs(x + 1, y), _dfs(x + 1, y + 1)
            d[x][y] = triangle[x][y] + min(left, right)
            return d[x][y]

        d = []
        for i in xrange(0, len(triangle)):
            d.append([float('-inf') for j in xrange(0, len(triangle[i]))])

        return _dfs(0, 0)

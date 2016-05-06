# -*- coding: utf-8 -*-

"""
Given a list of integer lists. Each time take an item from each list. Find all the combinations.
"""

class Solution(object):
    def combine(self, arr):
        """
        :type arr: List[List[init]]
        :rtype: List[List[int]]
        """
        def dfs(res, pos):
            if len(res) == len(arr):
                results.append(res)
                return

            for i in xrange(len(arr[pos])):
                dfs(res + [arr[pos][i]], pos + 1)

        results = []
        dfs([], 0)
        return results


if __name__ == '__main__':
    arr = [[1,2], [3,4], [5,6,7]]
    sol = Solution()
    print sol.combine(arr)

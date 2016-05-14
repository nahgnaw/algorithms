# -*- coding: utf-8 -*-

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(combination, pos):
            if len(combination) == k:
                results.append(combination)
                return

            for i in xrange(pos, n + 1):
                dfs(combination + [i], i + 1)

        results = []
        dfs([], 1)
        return results


    def combine2(self, n, k):
        results = []
        combination = []
        x = 1
        while True:
            l = len(combination)
            if l == k:
                results.append(combination[:])
            if l == k or x > n - k + l + 1:
                if not combination:
                    return results
                x = combination.pop() + 1
            else:
                combination.append(x)
                x += 1


if __name__ == '__main__':
    n, k = 5, 3
    sol = Solution()
    print sol.combine(n, k)
    print sol.combine2(n, k)
    print sol.combine3(n, k)

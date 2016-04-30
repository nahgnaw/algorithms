# -*- coding: utf-8 -*-

"""
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Note
You can not divide any item into small pieces.

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
"""


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size

    # sol[i][j]: the max size it can fill in a j size backpack with i items
    def backPack(self, m, A):
        if not A:
            return 0

        n = len(A)
        sol = [[0 for _ in xrange(m + 1)] for _ in xrange(n + 1)]
        for i in xrange(n + 1):
            for j in xrange(m + 1):
                if i == 0 or j == 0:
                    continue
                # If the ith item's size is larger than the capacity, it cannot be included.
                if A[i-1] > j:
                    sol[i][j] = sol[i-1][j]
                # For the ith item, it can be either included or not.
                else:
                    sol[i][j] = max(sol[i-1][j], sol[i-1][j-A[i-1]] + A[i-1])
        return sol[n][m]

    def backPack2(self, m, A):
        if not A:
            return 0

        n = len(A)
        sol = [0 for _ in xrange(m + 1)]
        for i in xrange(n):
            for j in xrange(m, -1, -1):
                if A[i] > j:
                    sol[j] = sol[j]
                else:
                    sol[j] = max(sol[j], sol[j-A[i]] + A[i])
        return sol[m]


if __name__ == '__main__':
    A = [2, 3, 5, 7]
    m = 11
    sol = Solution()
    print sol.backPack(m, A)
    print sol.backPack2(m, A)


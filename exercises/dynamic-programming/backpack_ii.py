# -*- coding: utf-8 -*-

"""
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?

Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Note
You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?
"""


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value

    # sol[i][j]: the max value it can fill in a j size backpack with i items
    def backPackII(self, m, A, V):
        if not A or not V or not m:
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
                    sol[i][j] = max(sol[i-1][j], sol[i-1][j-A[i-1]] + V[i-1])
        return sol[-1][-1]


    def backPackII2(self, m, A, V):
        if not A or not V or not m:
            return 0

        n = len(A)
        sol = [0 for j in xrange(m + 1)]
        for i in xrange(n):
            for j in xrange(m, -1, -1):
                if j >= A[i]:
                    sol[j] = max(sol[j], sol[j - A[i]] + V[i])

        return sol[m]


if __name__ == '__main__':
    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    m = 10
    sol = Solution()
    print sol.backPackII(m, A, V)
    print sol.backPackII2(m, A, V)

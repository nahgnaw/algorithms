# -*- coding: utf-8 -*-

"""
Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example
Given the permutation [1, 4, 2, 2], return 3.
"""


class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        import math

        def _dup_perm(hash_map):
            res = 1
            for val in hash_map.values():
                res *= math.factorial(val)
            return res

        if not A:
            return 0

        perm_index = 1
        for i in xrange(len(A)):
            rank = 0
            count_map = {A[i]: 1}
            for j in xrange(i + 1, len(A)):
                if A[j] < A[i]:
                    rank += 1
                count_map[A[j]] = count_map.setdefault(A[j], 0) + 1
            perm_index += rank * math.factorial(len(A) - 1 - i) / _dup_perm(count_map)

        return perm_index


if __name__ == '__main__':
    A = [1, 4, 2, 2]
    sol = Solution()
    print sol.permutationIndexII(A)

# -*- coding: utf-8 -*-

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)

        # Pre-generate factorials.
        factorial = [1]
        for i in xrange(1, n):
            factorial.append(i * factorial[-1])

        k -= 1  # Because of zero-based index.
        permutation = ''
        while n > 0:
            # Select the number from the left most digit.
            index = k / factorial[n-1]
            k = k % factorial[n-1]
            permutation += str(nums[index])
            nums.remove(nums[index])
            n -= 1

        return permutation


if __name__ == '__main__':
    n, k = 3, 5
    sol = Solution()
    print sol.getPermutation(n, k)

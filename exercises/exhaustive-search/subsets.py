# -*- coding: utf-8 -*-

"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    """
    Use bit manipulation.
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []

        results = []
        n = len(nums)
        nums.sort()

        for i in xrange(2 ** n):
            subset = []
            for j in xrange(n):
                if i & (1 << j):
                    subset.append(nums[j])
            results.append(subset)

        return results

    """
    Recursively use DFS to add elements to subsets.
    """
    def subsets2(self, nums):

        def dfs(nums, pos, temp_list, results):
            results.append([] + temp_list)

            for i in xrange(pos, len(nums)):
                temp_list.append(nums[i])
                dfs(nums, i + 1, temp_list, results)
                temp_list.pop()

        if nums is None:
            return []

        results = []
        nums.sort()
        dfs(nums, 0, [], results)
        return results

    """
    Iteratively add a new element to previous subsets.
    """
    def subsets3(self, nums):
        results = [[]]
        for num in sorted(nums):
            results += [item + [num] for item in results]
        return results

    # Recursion
    def subsets4(self, nums):

        def dfs(nums, pos, temp_list, results):
            results.append(temp_list[:])

            for i in xrange(pos, len(nums)):
                dfs(nums, i + 1, temp_list + [nums[i]], results)

        if nums is None:
            return []

        results = []
        nums.sort()
        dfs(nums, 0, [], results)
        return results



if __name__ == '__main__':
    nums = [2,3,1]
    sol = Solution()
    print sol.subsets(nums)
    print sol.subsets2(nums)
    print sol.subsets3(nums)
    print sol.subsets4(nums)


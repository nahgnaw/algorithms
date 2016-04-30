# -*- coding: utf-8 -*-

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(pos, temp_list):
            results.append(temp_list)

            for i in xrange(pos, len(nums)):
                if not i == pos and nums[i] == nums[i-1]:
                    continue
                dfs(i + 1, temp_list + [nums[i]])

        if nums is None:
            return []

        results = []
        nums.sort()
        dfs(0, [])
        return results

    def subsetsWithDup2(self, nums):
        results = [[]]
        size = 0
        nums.sort()
        for i in xrange(len(nums)):
            start = size if i > 0 and nums[i] == nums[i-1] else 0
            size = len(results)
            for j in xrange(start, size):
                results += [results[j] + [nums[i]]]
        return results

    def subsetsWithDup3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(pos, temp_list):
            results.append(temp_list)

            i = pos
            while i < len(nums):
                dfs(i + 1, temp_list + [nums[i]])
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1

        if nums is None:
            return []

        results = []
        nums.sort()
        dfs(0, [])
        return results

    
if __name__ == '__main__':
    nums = [1,1,1,1]
    sol = Solution()
    # print sol.subsetsWithDup(nums)
    # print sol.subsetsWithDup2(nums)
    print sol.subsetsWithDup3(nums)


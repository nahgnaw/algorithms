# -*- coding: utf-8 -*-

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _permuteUnique(pos):
            if pos == len(nums) - 1:
                results.add(tuple(nums[:]))
                return

            for i in xrange(pos, len(nums)):
                if not i == pos and nums[i] == nums[pos]:
                    continue
                nums[i], nums[pos] = nums[pos], nums[i]
                _permuteUnique(pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i] 

        results = set()
        _permuteUnique(0)
        return [list(tup) for tup in results]

    def permuteUnique2(self, nums):
        results = [[]]
        for n in nums:
            new_results = []
            for res in results:
                for i in xrange(len(res) + 1):
                    new_results.append(res[:i] + [n] + res[i:])
                    if i < len(res) and res[i] == n:
                        break
            results = new_results
        return results

    def permuteUnique3(self, nums):

        def dfs(tmp):
            if len(tmp) == len(nums):
                result.append(tmp)
                return
            
            i = 0
            while i < len(nums):
                if not visited[i]:
                    visited[i] = True
                    dfs(tmp + [nums[i]])
                    visited[i] = False
                    while i < len(nums) - 1 and nums[i] == nums[i+1]:
                        i += 1
                i += 1
        
        nums.sort()
        result = []
        visited = [False] * len(nums)
        dfs([])
        return result


if __name__ == '__main__':
    nums = [0, 1, 1, 0]
    sol = Solution()
    print sol.permuteUnique(nums)
    print sol.permuteUnique2(nums)
    print sol.permuteUnique3(nums)


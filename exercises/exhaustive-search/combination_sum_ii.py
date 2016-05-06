# -*- coding: utf-8 -*-

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(target, pos, combination):
            if target < 0:
                return
            if target == 0:
                results.append(combination)
                return
            for i in range(pos, len(candidates)):
                if not i == pos and candidates[i] == candidates[i-1]:
                    continue
                dfs(target - candidates[i], i + 1, combination + [candidates[i]])

        results = []
        candidates.sort()
        dfs(target, 0, [])
        return results

    def combinationSum2_1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(pos, tmp, target):
            if target < 0:
                return
            if target == 0:
                result.append(tmp)
                return
            
            i = pos
            while i < len(candidates):
                dfs(i + 1, tmp + [candidates[i]], target - candidates[i])
                while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                    i += 1
                i += 1
        
        candidates.sort()
        result = []
        dfs(0, [], target)
        return result
        

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sol = Solution()
    print sol.combinationSum2(candidates, target)
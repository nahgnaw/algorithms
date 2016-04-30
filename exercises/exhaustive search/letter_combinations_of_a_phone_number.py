# -*- coding: utf-8 -*-

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution(object):
    # Iterative
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        key_map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = ['']
        for d in digits:
            if not key_map[int(d)]:
                continue

            tmp = []
            chars = key_map[int(d)]
            for c in chars:
                for res in result:
                    tmp.append(res + c)
            result[:] = tmp

        return result


    # Backtracking
    def letterCombinations2(self, digits):
        if not digits:
            return []

        def dfs(result, pos, combination):
            if pos == len(digits):
                result.append(combination) 
                return 
            
            chars = key_map[int(digits[pos])]
            for c in chars:
                dfs(result, pos + 1, combination + c)

        key_map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        dfs(result, 0, '')
        return result

# -*- coding: utf-8 -*-

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""


class Solution(object):
    # O(nLlogL)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        sorted_strings = {}
        for s in strs:
            sorted_strings.setdefault(tuple(sorted(s)), []).append(s)

        for key in sorted_strings:
            sorted_strings[key] = sorted(sorted_strings[key])

        return sorted_strings.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print sol.groupAnagrams(strs)

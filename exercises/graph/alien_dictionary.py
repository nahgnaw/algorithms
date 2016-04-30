# -*- coding: utf-8 -*-

"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import deque
        
        char_set = set()
        for w in words:
            for c in w:
                char_set.add(c)
                
        # Compute indegrees for each character.
        # Get neighbors for each character.
        indegrees = {c: 0 for c in char_set}
        neighbors = {c: [] for c in char_set}
        for w in words:
            for i in xrange(len(w) - 1):
                if not w[i] == w[i+1]:
                    indegrees[w[i+1]] += 1
                    neighbors[w[i]].append(w[i+1])
        
        # Start from characters with 0 indegree.
        start = [c for c in indegrees if not indegrees[c]]
        if not start:
            return ''
            
        # Topological sort.
        order = []
        queue = deque(start)
        count = len(indegrees)
        while queue:
            char = queue.popleft()
            order.append(char)
            for c in neighbors[char]:
                indegrees[c] -= 1
                if not indegrees[c]:
                    queue.append(c)
            count -= 1
        # If count is not 0, it means there are cycles in the graph.
        return ''.join(order) if not count else ''
            
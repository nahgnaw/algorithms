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
    # BFS
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import deque
        
        if not words:
            return ''
            
        # Collect all the characters.
        char_set = set(''.join(words))
                
        # Build the graph.
        # A char's indegree is how many chars are before it.
        indegree = {c: 0 for c in char_set}
        neighbors = {c: [] for c in char_set}
        for pair in zip(words, words[1:]):
            for x, y in zip(*pair):
                if not x == y:
                    neighbors[x].append(y)  # x come before y
                    indegree[y] += 1
                    # Once an ordered pair is found, the rest char pairs 
                    # between the two words don't have order relations.
                    break
        
        # Collect the chars that have no other chars before them.
        first_chars = [c for c in indegree if indegree[c] == 0]
        if not first_chars:
            return ''
        
        queue = deque(first_chars)
        count = 0
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for c in neighbors[ch]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
            count += 1
        return ''.join(order) if count == len(char_set) else ''
        

        # DFS
        def alienOrder2(self, words):

            def dfs(ch):
                order.append(ch)
                for c in neighbors[ch]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        dfs(c)
        
            if not words:
                return ''
                
            # Collect all the characters.
            char_set = set(''.join(words))
                    
            # Build the graph.
            # A char's indegree is how many chars are before it.
            indegree = {c: 0 for c in char_set}
            neighbors = {c: [] for c in char_set}
            for pair in zip(words, words[1:]):
                for x, y in zip(*pair):
                    if not x == y:
                        neighbors[x].append(y)  # x come before y
                        indegree[y] += 1
                        # Once an ordered pair is found, the rest char pairs 
                        # between the two words don't have order relations.
                        break
            
            # Collect the chars that have no other chars before them.
            first_chars = [c for c in indegree if indegree[c] == 0]
            if not first_chars:
                return ''
            
            # Start DFS on chars whose indegrees are 0.     
            order = []
            for c in first_chars:
                dfs(c)
            # Cannot have cycle in the graph.
            return ''.join(order) if len(order) == len(char_set) else ''
        
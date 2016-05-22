# -*- coding: utf-8 -*-

"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be formed.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.
To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
"""


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(temp):
            if len(temp) == len(even_chars):
                results.append(''.join(temp))
                return
            
            i = 0
            while i < len(even_chars):
                if not visited[i]:
                    visited[i] = True
                    dfs(temp + [even_chars[i]])
                    visited[i] = False
                    while i < len(even_chars) - 1 and even_chars[i] == even_chars[i+1]:
                        i += 1
                i += 1
        
        if not s:
            return []
           
        # Collect character counts. 
        counts = {}
        for c in s:
            counts[c] = counts.setdefault(c, 0) + 1
            
        # Separate characters with odd counts and even counts.
        odd_chars, even_chars = [], []
        for char, count in counts.items():
            if count % 2:
                odd_chars.append(char)
            # Only keep half of the characters.
            for _ in xrange(count / 2):
                even_chars.append(char)
        
        # There can only be at most one character with even counts.            
        if len(odd_chars) > 1:
            return []
          
        # Sort character with odd counts.  
        even_chars.sort()
        visited = [False] * len(even_chars)
        results = []
        # Use backtracking to generate half of the palindromes.
        dfs([])
        
        # Append the other half.
        if odd_chars:
            return [res + odd_chars[0] + res[::-1] for res in results]
        return [res + res[::-1] for res in results]
        
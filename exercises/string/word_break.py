# -*- coding: utf-8 -*-

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # O(n^2)
        # dp[i]: whether s[:i] can be segmented.
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in xrange(1, len(s) + 1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                
        return dp[-1]
        
    # DFS
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        def dfs(pos):
            if pos == len(s):
                return True
                
            if pos in checked:
                return False
            
            for i in xrange(pos + 1, len(s) + 1):
                if s[pos:i] in wordDict:
                    if dfs(i):
                        return True
                    else:
                        checked.add(i)
            checked.add(pos)
            return False      
        
        checked = set()  # record if s[:i] is in the dictionary     
        return dfs(0)


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = Solution()
    print sol.wordBreak(s, wordDict)


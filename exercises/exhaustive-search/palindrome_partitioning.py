# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i]] + rest
                for i in xrange(1, len(s) + 1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition(s[i:])] or [[]]

    # Dynamic programming.
    def partition2(self, s):

        def isPalindrome(string):
            return string == string[::-1]

        if not s:
            return [[]]

        partitions = [[[]] for x in xrange(len(s) + 1)]
        partitions[1] = [[s[0]]]
        for i in xrange(1, len(s)):
            partitions[i+1] = []
            for j in xrange(0, i+1):
                if isPalindrome(s[j:i+1]):
                    for part in partitions[j]:
                        partitions[i+1].append(part + [s[j:i+1]])

        return partitions[len(s)]

    # Backtracking
    def partition3(self, s):

        def is_palindrome(string):
            return string == string[::-1]
            
        def dfs(string, tmp): 
            if not len(string):
                results.append(tmp)
                return
            
            for i in xrange(1, len(string) + 1):
                seg = string[:i]
                if is_palindrome(seg):
                    dfs(string[i:], tmp + [seg])
          
        if not s:
            return []
            
        results = []
        dfs(s, [])
        return results
        


if __name__ == '__main__':
    s = 'aabb'
    sol = Solution()
    print sol.partition(s)
    print sol.partition2(s)


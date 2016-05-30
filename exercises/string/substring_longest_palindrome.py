# -*- coding: utf-8 -*-

"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # dp[i][j]: whether s[i:j+1] is a palindrome
        dp = [[False] * n for k in xrange(n)]
        start_ind = 0
        max_len = 1

        for i in xrange(n):
            dp[i][i] = True

        for i in xrange(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start_ind = i
                max_len = 2

        for l in xrange(3, n+1):
            for i in xrange(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start_ind = i
                    max_len = l

        return s[start_ind:start_ind+max_len]

    # O(n^2). Go through every character, expanding from the middle to find palindrome.
    def longestPalindrome2(self, s):

        def get_palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest_palindrome = s[0]   # the shortest palindrome is a single character
        for i in xrange(len(s)):
            # Palindromes with odd lengths
            p = get_palindrome(i, i)
            if len(p) > len(longest_palindrome):
                longest_palindrome = p
            # Palindromes with even lengths
            p = get_palindrome(i, i+1)
            if len(p) > len(longest_palindrome):
                longest_palindrome = p
                
        return longest_palindrome


if __name__ == '__main__':
    s = 'abb'
    sol = Solution()
    print sol.longestPalindrome(s)
    print sol.longestPalindrome2(s)

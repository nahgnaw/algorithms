# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution(object):
    # Using a stack.
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        stack = []
        max_len = 0
        for i, c in enumerate(s):
            if c == ')':
                if stack and stack[-1][1] == '(':
                    stack.pop()
                    last = -1
                    if len(stack):
                        last = stack[-1][0]
                    max_len = max(max_len, i - last)
                else:
                    stack.append((i, c))
            else:
                stack.append((i, c))
        return max_len

    # DP.
    def longestValidParentheses2(self, s):
        # dp[i]: the length of the longest valid parentheses ending at index i in s.
        # dp[i] will always be 0 if s[i] == '('.
        # Return the maximum value in dp.
        dp = [0] * len(s)
        left_count = 0
        max_len = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                left_count += 1
            else:
                if left_count:
                    dp[i] = dp[i-1] + 2 # At least we have one more valid pair.
                    if i - dp[i] >= 0:
                        # We need to look beyond the current parenthesis closure that ends at i.
                        dp[i] += dp[i-dp[i]]
                    max_len = max(dp[i], max_len)
                    left_count -= 1
        return max_len

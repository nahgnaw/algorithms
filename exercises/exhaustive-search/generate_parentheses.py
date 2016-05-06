# -*- coding: utf-8 -*- 

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(left, right, temp):
            if left > right:
                return
            if left:
                generate(left - 1, right, temp + '(')
            if right:
                generate(left, right - 1, temp + ')')
            if not left and not right:
                result.append(temp)
                return

        result = []
        generate(n, n, "")
        return result

    def generateParenthesis2(self, n):
    
        def dfs(left, right, tmp):
            if not any([left, right]):
                result.append(tmp)
                return
            
            if left:
                dfs(left - 1, right, tmp + '(')
            if left < right:
                dfs(left, right - 1, tmp + ')')
        
        left = right = n
        result = []
        dfs(left, right, '')
        return result


if __name__ == '__main__':
    n = 4
    sol = Solution()
    print sol.generateParenthesis(n)
        
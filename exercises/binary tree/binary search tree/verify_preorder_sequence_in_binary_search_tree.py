# -*- coding: utf-8 -*-

"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """ 
        if len(preorder) <= 1:
            return True

        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True


if __name__ == '__main__':
    preorder = [1,2,3]
    sol = Solution()
    print sol.verifyPreorder(preorder)

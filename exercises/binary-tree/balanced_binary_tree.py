# -*- coding: utf-8 -*-

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Return depth.
        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        if not root:
            return True
        left, right = map(dfs, (root.left, root.right))
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced2(self, root):

        def dfs(root):
            if not root:
                return 0, True
            left_heigt, left_balance = dfs(root.left)
            right_heigt, right_balance = dfs(root.right)
            balance = abs(left_heigt - right_heigt) <= 1
            return max(left_heigt, right_heigt) + 1, left_balance and right_balance and balance

        return dfs(root)[1]

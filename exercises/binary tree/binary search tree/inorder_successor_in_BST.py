# -*- coding: utf-8 -*-

"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val >= p.val:
                    successor.append(root)
                if len(successor) > 2:
                    break
                root = root.right
        return successor[1] if len(successor) > 1 else None

    def inorderSuccessor2(self, root, p):
        successor = None
        while root is not None:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    def inorderSuccessor3(self, root, p):
        if root is None:
            return None
        if root.val > p.val: 
            return self.inorderSuccessor3(root.left, p) or root
        return self.inorderSuccessor3(root.right, p)
# -*- coding: utf-8 -*- 

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursive
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _is_valid(root, upper, lower):
            if root is None:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            return _is_valid(root.left, root.val, lower) and _is_valid(root.right, upper, root.val)

        return _is_valid(root, float('inf'), float('-inf'))

    # The inorder traversal or a binary search tree should produce an ascending ordered list.
    def isValidBST2(self, root):
        def inorder(root, output):
            if root is not None:
                inorder(root.left, output)
                output.append(root.val)
                inorder(root.right, output)

        if root is None:
            return True

        output = []
        inorder(root, output)
        for i in xrange(len(output) - 1):
            if output[i] >= output[i+1]:
                return False
        return True

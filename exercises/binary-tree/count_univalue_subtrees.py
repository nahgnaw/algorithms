# -*- coding:utf8 -*-

"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        count = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if self.isUnivalTree(node):
                count += 1
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return count

    def isUnivalTree(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if (root.left is None and root.val == root.right.val) or \
           (root.right is None and root.val == root.left.val) or \
           (root.left is not None and root.right is not None and root.val == root.left.val == root.right.val):
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return False


    def countUnivalSubtrees2(self, root):
        count = [0]
        self.isUnivalTree2(root, count)
        return count[0]

    def isUnivalTree2(self, root, count):
        if root is None:
            return True

        left = self.isUnivalTree2(root.left, count)
        right = self.isUnivalTree2(root.right, count)

        if not left or not right:
            return False

        if root.left is not None and not root.val == root.left.val:
            return False

        if root.right is not None and not root.val == root.right.val:
            return False

        count[0] += 1
        return True


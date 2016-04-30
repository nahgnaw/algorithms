# -*- coding: utf-8 -*-

"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursive
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        root.left, root.right = root.right, root.left
        map(self.invertTree, (root.left, root.right))
        return root


    # DFS
    def invertTree2(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                map(stack.append, (node.left, node.right))
        return root

    # BFS
    def invertTree3(self, root):
        from collections import deque

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                map(queue.append, (node.left, node.right))
        return root

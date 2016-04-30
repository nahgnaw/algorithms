# -*- coding: utf-8 -*-

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursive
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root:
                return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

    # DFS
    def maxDepth2(self, root):
        if not root:
            return 0

        depth = 1
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            depth = max(level, depth)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return depth

    # BFS
    def maxDepth3(self, root):
        if not root:
            return 0

        from collections import deque
        q = deque()
        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right and not q:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
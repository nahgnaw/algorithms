# -*- coding: utf-8 -*- 


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # DFS
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)

    # BFS
    def minDepth2(self, root):
        from collections import deque

        if root is None:
            return 0
        q = deque([(root, 1)])
        while len(q):
            node, dep = q.popleft()
            if node:
                if not node.left and not node.right:
                    return dep
                else:
                    q.append((node.left, dep + 1))
                    q.append((node.right, dep + 1))
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        if not root:
            return []

        result = []
        q = deque()
        q.append([root])

        while q:
            nodes = q.popleft()
            level = []
            level_values = []
            for node in nodes:
                level_values.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                q.append(level)
            result.append(level_values)
        return result

    def levelOrder(self, root):
        result, level = [], [root]
        while root and level:
            result.append([node.val for node in level])
            children = [(node.left, node.right) for node in level]
            level = [child for pair in children for child in pair if child]
        return result

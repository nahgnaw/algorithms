# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        nodes = [root]
        level = 0
        while root and nodes:
            level += 1
            if not level % 2:
                result.append([node.val for node in nodes[::-1]])
            else:
                result.append([node.val for node in nodes])
            children = [(node.left, node.right) for node in nodes]
            nodes = [node for pair in children for node in pair if node]
        return result

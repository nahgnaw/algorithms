# -*- coding: utf-8 -*- 

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result, level = [], [root]
        while level and root:
            result.append([node.val for node in level])
            children = [(node.left, node.right) for node in level]
            level = [child for pair in children for child in pair if child]
        return result[::-1]

    def levelOrderBottom2(self, root):

        def dfs(root, level):
            if root:
                if len(result) < level + 1:
                    result.insert(0, [])
                result[-(level+1)].append(root.val)
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)

        result = []
        dfs(root, 0)
        return result
        
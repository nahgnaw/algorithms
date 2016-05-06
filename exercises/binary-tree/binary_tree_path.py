# -*- coding: utf-8 -*-

"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursion
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path):
            if root.left is None and root.right is None:
                path.append(str(root.val))
                path = '->'.join(path)
                result.append(path)
            if root.left is not None:
                dfs(root.left, path + [str(root.val)])
            if root.right is not None:
                dfs(root.right, path + [str(root.val)])

        if root is None:
            return []
            
        result = []
        dfs(root, [])
        return result

    # DFS + stack
    def binaryTreePaths2(self, root):
        if root is None:
            return []
            
        result, stack = [], [(root, [])]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                path.append(str(node.val))
                result.append('->'.join(path))
            if node.left is not None:
                stack.append((node.left, path + [str(node.val)]))
            if node.right is not None:
                stack.append((node.right, path + [str(node.val)]))
        return result

    
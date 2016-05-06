# -*- coding: utf-8 -*-

"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Hint:

You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _is_bst(root, lower, upper):
            if root is None:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return _is_bst(root.left, lower, root.val) and _is_bst(root.right, root.val, upper)

        def _count_nodes(root):
            if root is None:
                return 0
            return 1 + _count_nodes(root.left) + _count_nodes(root.right)

        if root is None:
            return 0

        if _is_bst(root, float('-inf'), float('inf')):
            return _count_nodes(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))


    def largestBSTSubtree2(self, root):
        def dfs(root):
            if root is None:
                return 0, 0, float('inf'), float('-inf')

            left_largest, left_nodes, left_min, left_max = dfs(root.left)
            right_largest, right_nodes, right_min, right_max = dfs(root.right)
            nodes = 1 + left_nodes + right_nodes if left_max < root.val < right_min else float('-inf')
            return max(left_largest, right_largest, nodes), nodes, min(left_min, root.val), max(right_max, root.val)

        return dfs(root)[0]

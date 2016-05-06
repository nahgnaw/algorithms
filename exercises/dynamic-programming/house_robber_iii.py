# -*- coding: utf-8 -*-

"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_subtree(node):
            if node is None:
                # The 1st returned element is the amount of money if subtree node is not robbed.
                # The 2nd returned element is the amount of money if subtree node is robbed.
                return [0, 0]
                
            money = [0, 0]
            left = rob_subtree(node.left)
            right = rob_subtree(node.right)
            
            # If node is not robbed, its children can be robbed or not.
            money[0] = max(left[0], left[1]) + max(right[0], right[1])
            # If node is robbed, its children cannot be robbed.
            money[1] = node.val + left[0] + right[0]
            
            return money
            
        return max(rob_subtree(root))
        
# -*- coding: utf-8 -*-

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, cur_sum, temp_list):
            if node is None:
                return 
            
            if node.left is None and node.right is None:
                if node.val == cur_sum:
                    results.append(temp_list + [node.val])
                return
            
            dfs(node.left, cur_sum - node.val, temp_list + [node.val])
            dfs(node.right, cur_sum - node.val, temp_list + [node.val])
        
        results = []
        dfs(root, sum, [])
        return results
        
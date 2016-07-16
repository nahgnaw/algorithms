# -*- coding: utf-8 -*-

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # DFS. Recursive.
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, last_val, tmp_len):
            if node is None:
                return
            
            # If the sequence is consectively increasing, 
            # increment tmp_len and update max_len
            if node.val == last_val + 1:
                tmp_len += 1
                max_len[0] = max(max_len[0], tmp_len)
            # Otherwise reset tmp_len
            else:
                tmp_len = 1
                
            for child in [node.left, node.right]:
                dfs(child, node.val, tmp_len)
        
          
        if root is None:
            return 0
            
        max_len = [1]
        dfs(root, root.val, 1)
        return max_len[0]

    # DFS. Iterative.
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        max_len = 1
        stack = [(root, 1)]
        while stack:
            node, cur_len = stack.pop()
            if node.left:
                stack.append((node.left, cur_len + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cur_len + 1 if node.right.val == node.val + 1 else 1))
            max_len = max(max_len, cur_len)
        return max_len


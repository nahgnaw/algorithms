# -*- coding: utf-8 -*-

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(left, right):
            if left is None or right is None:
                return left == right
            if not left.val == right.val:
                return False
            return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)
        
        if root is None:
            return True
        return _isSymmetric(root.left, root.right)

    # Iterative
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        
        if root is None:
            return True
            
        q = deque([[root]])
        while q:
            nodes = q.popleft()
            level = []
            for node in nodes:
                level.append(node.left)
                level.append(node.right)
                
            left, right = 0, len(level) - 1
            while left < right:
                if level[left] is None and level[right] is None:
                    left += 1
                    right -= 1
                    continue
                if level[left] is None or level[right] is None:
                    return False
                if not level[left].val == level[right].val:
                    return False
                left += 1
                right -= 1
                
            level = [n for n in level if n]
            if level:
                q.append(level)
        return True

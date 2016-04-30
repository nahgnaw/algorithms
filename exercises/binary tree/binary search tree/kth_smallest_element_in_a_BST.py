# -*- coding: utf-8 -*-

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Inorder traversal
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right

    def kthSmallest2(self, root, k):
        left_count = self.count_node(root.left)
        if left_count + 1 == k:
            return root.val
        elif left_count + 1 < k:
            return self.kthSmallest2(root.right, k - 1 - left_count)
        else:
            return self.kthSmallest2(root.left, k)

    def count_node(self, root):
        if root is None:
            return 0
        return 1 + self.count_node(root.left) + self.count_node(root.right)

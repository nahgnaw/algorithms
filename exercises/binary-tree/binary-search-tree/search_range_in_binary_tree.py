# -*- coding: utf-8 -*-

"""
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):

        def _inorder(root, k1, k2, output):
            if root is None:
                return

            if root is not None and root.val > k1:
                _inorder(root.left, k1, k2, output)

            if k1 <= root.val <= k2:
                output.append(root.val)

            if root is not None and root.val < k2:
                _inorder(root.right, k1, k2, output)

        output = []
        _inorder(root, k1, k2, output)
        return output

    def searchRange2(self, root, k1, k2):
        stack = []
        output = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if k1 <= root.val <= k2:
                    output.append(root.val)
                elif root.val > k2:
                        break 
                root = root.right
        return output

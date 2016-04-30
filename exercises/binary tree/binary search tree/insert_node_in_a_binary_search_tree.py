# -*- coding:utf8 -*-

"""
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6
"""



# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if root is None:
            return node
        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

    def insertNode2(self, root, node):
        if root is None:
            return node
        if node is None:
            return root

        rootcopy = root
        while root is not None:
            if node.val > root.val and root.right is None:
                root.right = node
                break
            elif node.val < root.val and root.left is None:
                root.left = node
                break
            elif node.val > root.val:
                root = root.right
            else:
                root = root.left
        return rootcopy

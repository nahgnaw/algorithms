# -*- coding: utf-8 -*-

"""
Given preorder traversal of a binary search tree, construct the binary search tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # O(n^2)
    def build_BST(self, preorder):
        if preorder:
            root = TreeNode(preorder.pop(0))
            i = 0
            while i < len(preorder) and preorder[i] < root.val:
                i += 1
            root.left = self.build_BST(preorder[:i])
            root.right = self.build_BST(preorder[i:])
            return root
        return None

    # O(n)
    def build_BST2(self, preorder):
        def helper(left, right):
            node = None
            if index[0] < len(preorder) and left < preorder[index[0]] < right:
                value = preorder[index[0]]
                node = TreeNode(value)
                index[0] += 1
                node.left = helper(left, value)
                node.right = helper(value, right)
            return node

        index = [0]
        return helper(float('-inf'), float('inf'))


    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)



if __name__ == '__main__':
    sol = Solution()
    preorder = [6,4,2,1,3,5,8,7,9]
    root = sol.build_BST2(preorder)
    print sol.inorder_traversal(root)

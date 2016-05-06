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
    def build_BST(self, postorder):
        if postorder:
            root = TreeNode(postorder.pop())
            i = len(postorder) - 1
            while i > -1 and postorder[i] > root.val:
                i -= 1
            root.right = self.build_BST(postorder[i+1:])
            root.left = self.build_BST(postorder[:i+1])
            return root
        return None

    # O(n)
    def build_BST2(self, postorder):
        def helper(left, right):
            node = None
            if index[0] > -1 and left < postorder[index[0]] < right:
                val = postorder[index[0]]
                index[0] -= 1
                node = TreeNode(val)
                node.right = helper(val, right)
                node.left = helper(left, val)
            return node

        index = [len(postorder) - 1]
        return helper(float('-inf'), float('inf'))


    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)



if __name__ == '__main__':
    sol = Solution()
    postorder = [1,3,2,5,4,7,9,8,6]
    root = sol.build_BST2(postorder)
    print sol.inorder_traversal(root)


# -*- coding: utf-8 -*-


"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder, inorder):
        if inorder:
            root_value = preorder.pop(0)
            root_index = inorder.index(root_value)
            root_node = TreeNode(root_value)
            root_node.left = self.buildTree2(preorder, inorder[:root_index])
            root_node.right = self.buildTree2(preorder, inorder[root_index+1:])
            return root_node
        return None

    def buildTree2(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        if not len(preorder) == len(inorder):
            return None

        dummy = TreeNode(0)
        inorder_map = {inorder[ind] : ind for ind in xrange(len(inorder))}
        preorder = preorder[::-1]
        stack = [(0, len(inorder) - 1 , dummy, True)]
        while stack:
            start, end, parent, is_left = stack.pop()
            node = TreeNode(preorder.pop())
            if is_left:
                parent.left = node
            else:
                parent.right = node
            index = inorder_map[node.val]
            if index < end:
                stack.append((index + 1, end, node, False))
            if index > start:
                stack.append((start, index - 1, node, True))
        return dummy.left


if __name__ == '__main__':
    inorder = [4,2,5,1,3,6]
    preorder = [1,2,4,5,3,6]
    sol = Solution()
    print sol.buildTree2(preorder, inorder)

# -*- coding: utf-8 -*-

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_node = TreeNode(postorder.pop())
            root_index = inorder.index(root_node.val)
            root_node.right = self.buildTree(inorder[root_index+1:], postorder)
            root_node.left = self.buildTree(inorder[:root_index], postorder)
            return root_node
        return None

    def buildTree2(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        if not len(postorder) == len(inorder):
            return None

        dummy = TreeNode(0)
        inorder_map = {inorder[ind] : ind for ind in xrange(len(inorder))}
        stack = [(0, len(inorder) - 1, dummy, True)]
        while stack:
            start, end, parent, is_left = stack.pop()
            node = TreeNode(postorder.pop())
            if is_left:
                parent.left = node
            else:
                parent.right = node
            index = inorder_map[node.val]
            if index > start:
                stack.append((start, index - 1, node, True))
            if index < end:
                stack.append((index + 1, end, node, False))
            
        return dummy.left


if __name__ == '__main__':
    inorder = [4,2,5,1,3,6]
    postorder = [4,5,2,6,3,1]
    sol = Solution()
    print sol.buildTree2(inorder, postorder)

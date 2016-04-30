# -*- coding: utf-8 -*-

"""
Binary tree traversal.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Traversal(object):

    def preorder_recursive(root):
        if root is None:
            return []
        return self.preorder_recursive(root.left) + [root.val] + self.preorder_recursive(root.right)

    def inorder_recursive(root):
        if root is None:
            return []
        return [root.val] + self.inorder_recursive(root.left) + self.inorder_recursive(root.right)

    def postorder_recursive(root):
        if root is None:
            return []
        return self.postorder_recursive(root.left) + self.postorder_recursive(root.right) + [root.val]

    def preorder_iterative(root):
        stack, result = [], []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return result

    def inorder_iterative(root):
        stack, result = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = root.right
            return result

    def postorder_iterative(root):
        stack, result = [], []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root.right)
                root = root.right
            else:
                root = stack.pop().left
        return result[::-1]

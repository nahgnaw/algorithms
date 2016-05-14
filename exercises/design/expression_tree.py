# -*- coding: utf-8 -*-

"""
Construct a binary expression tree given postfix expression.
"""


class ExressionTree(object):

    operators = '+-*/^'

    class TreeNode(object):
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.inorder = []

    def is_operator(self, c):
        return c in ExressionTree.operators

    def inorder_traversal(self, root):
        if root is None:
            return
        if self.is_operator(root.val):
            self.inorder.append('(')
        self.inorder_traversal(root.left)
        self.inorder.append(root.val)
        self.inorder_traversal(root.right)
        if self.is_operator(root.val):
            self.inorder.append(')')

    def get_inorder(self):
        return ''.join(self.inorder)

    def construct_tree(self, expression):
        stack = []
        for c in expression:
            if not self.is_operator(c):
                stack.append(self.TreeNode(c))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                node = self.TreeNode(c)
                node.left, node.right = op2, op1
                stack.append(node)
        return stack.pop()


if __name__ == '__main__':
    expression = 'abc-*'
    et = ExressionTree()
    root = et.construct_tree(expression)
    et.inorder_traversal(root)
    print et.get_inorder()


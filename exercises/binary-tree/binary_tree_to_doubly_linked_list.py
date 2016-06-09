# -*- coding: utf-8 -*-

"""
Convert a binary tree to a doubly linked list. The order of the nodes in the list must be the same as the inorder traversal of the tree.
"""


# Node definition of the binary tree and the doubly linked list.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # Return the head and the tail of the doubly linked list converted from the tree rooted at the given node.
    def tree_to_list(self, node):
        # Empty node
        if node is None:
            return None, None
        # Single node
        elif node.left is None and node.right is None:
            return node, node
        # No left child
        elif node.left is None:
            head, tail = self.tree_to_list(node.right)
            node.right = head
            head.left = node
            return node, tail
        # No right child
        elif node.right is None:
            head, tail = self.tree_to_list(node.left)
            node.left = tail
            tail.right = node
            return head, node
        # Both left and right children are present
        else:
            left_head, left_tail = self.tree_to_list(node.left)
            node.left = left_tail
            left_tail.right = node
            right_head, right_tail = self.tree_to_list(node.right)
            node.right = right_head
            right_head.left = node
            return left_head, right_tail


if __name__ == '__main__':
    a, b, c = Node(1), Node(2), Node(3)
    b.left, b.right = a, c

    sol = Solution()
    head, tail = sol.tree_to_list(b)

    while head:
        print head.val
        head = head.right
    while tail:
        print tail.val
        tail = tail.left

# -*- coding: utf-8 -*-

"""
Convert a sorted linked list to a balanced BST.
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def linked_list_to_bst(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        prev, middle = self.get_middle_node(head)
        if prev is not None:
            prev.next = None
        root = TreeNode(middle.val)
        root.left = self.linked_list_to_bst(head)
        root.right = self.linked_list_to_bst(middle.next)
        return root

    def get_middle_node(self, head):
        if head is None:
            return None, None
        if head.next is None:
            return None, head

        slow = fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow

    def bst_inorder(self, root):
        if root is None:
            return []

        inorder = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                inorder.append(node.val)
                root = node.right
        return inorder


if __name__ == '__main__':
    head = ListNode(1)
    walk = head
    for i in xrange(2, 11):
        walk.next = ListNode(i)
        walk = walk.next

    sol = Solution()
    root = sol.linked_list_to_bst(head)
    print sol.bst_inorder(root)

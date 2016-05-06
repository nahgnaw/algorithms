# -*- coding: utf-8 -*-

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def _sorted_list_to_bst(head, list_length):
            if not list_length :
                return None

            mid = (list_length - 1)/ 2
            count = mid
            cur = head
            while count:
                cur = cur.next
                count -= 1
            root = TreeNode(cur.val)
            root.left = _sorted_list_to_bst(head, mid)
            root.right = _sorted_list_to_bst(cur.next, list_length - mid - 1)

            return root

        if head is None:
            return None

        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        return _sorted_list_to_bst(head, list_len)
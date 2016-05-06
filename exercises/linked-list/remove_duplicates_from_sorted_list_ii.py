# -*- coding: utf-8 -*-

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next is not None and cur.next.next is not None:
            if cur.next.val == cur.next.next.val:
                node = cur.next
                while node.next is not None and node.val == node.next.val:
                    dup = node.next
                    node.next = dup.next
                    dup = None
                cur.next = node.next
                node = None
            else:
                cur = cur.next

        return dummy.next




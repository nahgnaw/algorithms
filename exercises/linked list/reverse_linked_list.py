# -*- coding: utf-8 -*-

"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def recursivelyReverseList(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.recursiveReverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

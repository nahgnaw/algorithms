# -*- coding: utf-8 -*-

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
            
        # Find out the length of the list and the tail position.
        length = 0 
        walk = head
        tail = head
        while walk is not None:
            length += 1
            if walk.next is None:
                tail = walk
            walk = walk.next
            
        # Make the list a circle.
        tail.next = head
            
        # Find the new head and the new tail.
        k = k % length
        for _ in xrange(length - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
            
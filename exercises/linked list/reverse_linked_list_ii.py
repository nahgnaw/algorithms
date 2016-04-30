# -*- coding: utf-8 -*-

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        for i in xrange(m - 1):
            head = head.next

        prev_m = head
        m_node = head.next
        n_node = m_node
        post_n = m_node.next
        for i in xrange(m, n):
            temp = post_n.next
            post_n.next = n_node
            n_node = post_n
            post_n = temp

        prev_m.next = n_node
        m_node.next = post_n

        return dummy.next

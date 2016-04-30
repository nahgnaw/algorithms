# -*- coding: utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        dummy = node = ListNode(0)

        h = [(n.val, n) for n in lists if n]
        heapq.heapify(h)

        while h:
            val, n = h[0]
            if n.next is None:
                heapq.heappop(h)
            else:
                heapq.heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next
# -*- coding: utf-8 -*-

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def print_list(self, head):
        if head is None:
            print None

        walk = head
        while walk is not None:
            print walk.val,
            walk = walk.next

    # Merge sort. Space: O(nlogn).
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Merge two lists.
        def merge(h1, h2):
            dummy = tail = ListNode(0)
            while h1 is not None and h2 is not None:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next
            # Append whichever is left.
            tail.next = h1 or h2
            return dummy.next
            
        if head is None or head.next is None:
            return head
            
        pre, slow, fast = None, head, head
        # Split the original list into two lists.
        while fast is not None and fast.next is not None:
            # When fast reaches the end, slow will be in the middle.
            pre, slow, fast = slow, slow.next, fast.next.next
        # Cut the list into two.
        pre.next = None
        
        # Recursively split the original list and merge two by two.
        return merge(*map(self.sortList, (head, slow)))

    # Quick sort.
    def sortList2(self, head):

        def get_tail(head):
            walk = head
            while walk is not None and walk.next is not None:
                walk = walk.next
            return walk

        def partition(head, tail):
            # Use the tail node as the pivot.
            pivot = tail

            prev = dummy = ListNode(0)
            dummy.next = head
            while not head == pivot:
                # Nodes smaller than the pivot stay where they were.
                if head.val < pivot.val:
                    prev = head
                    head = head.next
                # Nodes greater than the pivot are moved after the pivot.
                else:
                    left_next = head.next
                    prev.next = left_next
                    tail.next = head
                    tail = head
                    tail.next = None
                    head = left_next

            return dummy.next, tail, pivot


        def quick_sort(head, tail):
            if head is None or head == tail:
                return head

            # Divide the list. Return the pivot node.
            # The head and the tail of the original list will get changed during the partition.
            new_head, new_tail, pivot = partition(head, tail)
            # If the pivot happens to be the smallest node, no need to sort the left half of the list.
            if not new_head == pivot:
                # Cut the list at the pivot.
                walk = new_head
                while not walk.next == pivot:
                    walk = walk.next
                walk.next = None

                # Recur on the left half of the list.
                new_head = quick_sort(new_head, walk)

                # Reconnect the two halves.
                get_tail(new_head).next = pivot

            # Recur on the right half of the list.
            pivot.next = quick_sort(pivot.next, new_tail)

            return new_head

        if head is None or head.next is None:
            return head

        return quick_sort(head, get_tail(head))


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    new_head = sol.sortList2(head)
    sol.print_list(new_head)

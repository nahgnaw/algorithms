# -*- coding: utf-8 -*-

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse_list(h):
            prev = None
            while h is not None:
                next = h.next
                h.next = prev
                prev = h
                h = next
            return prev
                
        if head is None or head.next is None:
            return True
            
        prev = None
        slow = fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None    # Cut the list into halves
        
        first_half, second_half = head, None
        # Even number of nodes:
        if fast is None:
            second_half = reverse_list(slow)
        # Odd number of nodes:
        else:
            second_half = reverse_list(slow.next)
        
        while first_half is not None:
            if not first_half.val == second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True

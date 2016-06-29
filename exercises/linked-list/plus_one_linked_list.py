# -*- coding: utf-8 -*-

"""
Given a non-negative number represented as a singly linked list of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(h):
            prev = None
            while h is not None:
                next = h.next
                h.next = prev
                prev = h
                h = next
            return prev
            
        if head is None:
            return None
        
        # Put head at the least significant digit    
        head = reverse(head)
        
        walk = head
        prev = None
        carry = 1
        while walk is not None:
            sum = walk.val + carry
            walk.val = sum % 10
            carry = sum / 10
            if not carry:
                break
            prev = walk
            walk = walk.next
        # Append "1" in case of the most significant digit is 9
        if carry:
            prev.next = ListNode(1)
        return reverse(head)
        
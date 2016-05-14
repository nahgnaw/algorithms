# -*- coding: utf-8 -*-

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # O(n). Two passes. Using dictionary.
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes = {}
        walk = head
        while walk:
            nodes[walk] = RandomListNode(walk.label)
            walk = walk.next
            
        walk = head
        while walk:
            nodes[walk].next = nodes.get(walk.next)
            nodes[walk].random = nodes.get(walk.random)
            walk = walk.next
            
        return nodes.get(head)


    # O(n). Three passes. No extra space.
    def copyRandomList2(self, head):
        if not head:
            return None

        # 1st pass: create a node copy after each original node.
        walk = head
        while walk:
            copy = RandomListNode(walk.label)
            copy.next = walk.next
            walk.next = copy
            walk = walk.next.next

        # 2nd pass: assign the random pointer for each node copy.
        walk = head
        while walk:
            if walk.random:
                walk.next.random = walk.random.next
            walk = walk.next.next

        # 3rd pass: separate copied nodes from the original list.
        new_head = head.next
        walk = head
        new_walk = new_head
        while new_walk.next:
            walk.next = new_walk.next
            walk = walk.next
            new_walk.next = walk.next
            new_walk = new_walk.next
        # Finally, cut the link between walk and new_walk.
        walk.next = None
        new_walk.next = None

        return new_head
        
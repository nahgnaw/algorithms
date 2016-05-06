# -*- coding: utf-8 -*-

"""
Print nodes' values on a specific level of a binary tree.
"""


class Solution(object):
    def print_level(root, k):
        from collections import deque

        if root is None:
            print None

        queue = deque([])
        queue.append(([root], 0))
        while queue:
            nodes, level = queue.popleft()
            if level == k:
                print [node.val for node in nodes]
                break
            else:
                children = []
                for node in nodes:
                    if node.left is not None:
                        children.append(node.left)
                    if node.right is not None:
                        children.append(node.right)
                if children:
                    queue.append(children, level + 1)

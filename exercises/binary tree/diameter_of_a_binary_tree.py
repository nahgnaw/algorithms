# -*- coding: utf-8 -*-

"""
The diameter of a tree (sometimes called the width) is the number of nodes
on the longest path between two leaves in the tree.
The diagram below shows two trees each with diameter nine,
the leaves that form the ends of a longest path are shaded
(note that there is more than one path in each tree of length nine,
but no path longer than nine nodes).
"""


class Solution(object):
    def get_diameter(self, root):
        if root is None:
            return 0

        left_height, right_height = map(self.get_height, (root.left, root.right))
        left_diameter, right_diameter = map(self.get_diameter, (root.left, root.right))
        max_diameter = max(left_diameter, right_diameter)
        return max(max_diameter, 1 + left_height + right_height)


    def get_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

# -*- coding: utf-8 -*-

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parents = set()
        while p is not None or q is not None:
            if p in parents:
                return p
            if q in parents:
                return q
            parents.add(p)
            parents.add(q)
            p = p.parent
            q = q.parent

    def lowestCommonAncestor2(self, p, q):
        def get_level(node):
            walk = node
            level = 0
            while walk.parent is not None:
                walk = walk.parent
                level += 1
            return level

        # Move p and q to the same level.
        level_diff = get_level(p) - get_level(q)
        diff = level_diff
        while abs(diff):
            if diff < 0:
                q = q.parent
            else:
                p = p.parent
            diff -= 1

        if p == q:
            if level_diff < 0:
                return p
            else:
                return q

        while not p == q:
            p = p.parent
            q = q.parent
        return p



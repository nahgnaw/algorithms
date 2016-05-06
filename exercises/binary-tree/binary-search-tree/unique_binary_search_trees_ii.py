# -*- coding: utf-8 -*-

"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.build_tree(1, n + 1)

    def build_tree(self, start, end):
        if start == end:
            return None

        nodes = []
        for i in xrange(start, end):
            for left in self.build_tree(start, i) or [None]:
                for right in self.build_tree(i+1, end) or [None]:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    nodes.append(root)
        return nodes


if __name__ == '__main__':
    n = 0
    sol = Solution()
    print sol.generateTrees(n)

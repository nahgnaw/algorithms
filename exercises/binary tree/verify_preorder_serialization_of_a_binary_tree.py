# -*- coding: utf-8 -*-

"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""


class Solution(object):
    # Consider # nodes as leaves.
    # For a full binary tree, number of leaves == number of middle nodes + 1
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False

        depth = 0
        for i in preorder.split(',')[:-1]:
            if i == '#':
                if depth == 0:
                    return False
                depth -= 1
            else:
                depth += 1
        if depth:
            return False
        return preorder[-1] == '#'

    # For a full binary tree, total indegree == total outdegree
    def isValidSerialization2(self, preorder):
        if not preorder:
            return False
        
        degree_sum = 1
        for x in preorder.split(','):
            degree_sum -= 1
            if degree_sum < 0:
                return False
            if not x == '#':
                degree_sum += 2
        return degree_sum == 0


if __name__ == '__main__':
    preorder = '#'
    sol = Solution()
    print sol.isValidSerialization2(preorder)

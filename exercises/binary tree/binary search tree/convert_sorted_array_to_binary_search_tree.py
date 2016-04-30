# -*- coding: utf-8 -*-


"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

    def sortedArrayToBST2(self, nums):
        if not nums:
            return None
            
        preorder = []
        self.buildPreorder(0, len(nums) - 1, nums, preorder)
        
        dummy = TreeNode(0)
        inorder_map = {nums[i]:i for i in xrange(len(nums))}
        preorder = preorder[::-1]
        stack = [(0, len(nums) - 1, dummy, True)]
        while stack:
            start, end, parent, is_left = stack.pop()
            node = TreeNode(preorder.pop())
            if is_left:
                parent.left = node
            else:
                parent.right = node
            index = inorder_map[node.val]
            if index < end:
                stack.append((index + 1, end, node, False))
            if index > start:
                stack.append((start, index - 1, node, True))
        return dummy.left


    def buildPreorder(self, start, end, nums, preorder):
        if start <= end:
            mid = (start + end) / 2
            preorder.append(nums[mid])
            self.buildPreorder(start, mid - 1, nums, preorder)
            self.buildPreorder(mid + 1, end, nums, preorder)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    sol = Solution()
    print sol.sortedArrayToBST2(nums)
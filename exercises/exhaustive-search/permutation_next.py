# -*- coding: utf-8 -*-

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    """
    1. Loop over the list from the right-hand side, if all the elements is in ascending order, just return the reversed list.
    2. Starting from the right-hand side, find the first element (named A) that breaks the ascending order.
    3. Starting from the right-hand side, find the first element (named B) that is larger than A. Swap A and B.
    4. Reverse all the elements on the right of the position of current A.
    """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in xrange(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = nums[len(nums)-1:i:-1]
                break
            elif i == 0:
                nums[:] = nums[::-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    sol.nextPermutation(nums)
    print nums

# -*- coding: utf-8 -*-

"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Note
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Challenge
Can you partition the array in-place and in O(n)?
"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    # O(n)
    def partitionArray(self, nums, k):
        par = 0
        for i in xrange(len(nums)):
            if nums[i] < k:
                nums[i], nums[par] = nums[par], nums[i]
                par += 1
        return par

    # O(n)
    def partitionArray2(self, nums, k):
        left, right = 0, len(nums) - 1
        if left >= right:
            return 0

        while left < right:
            while left <= right and nums[right] >= k:
                right -= 1
            while left <= right and nums[left] < k:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left


if __name__ == '__main__':
    nums = [7,7,9,8,6,6,8,7,9,8,6,6]
    k = 4
    sol = Solution()
    print sol.partitionArray(nums, k)
    print sol.partitionArray2(nums, k)

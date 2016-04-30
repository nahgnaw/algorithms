# -*- coding: utf-8 -*-

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = [nums[(n-k+i)%n] for i in xrange(n)]

    def rotate2(self, nums, k):
        def _swap(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k % n
        _swap(nums, 0, n - 1)
        _swap(nums, 0, k - 1)
        _swap(nums, k, n - 1)


if __name__ == '__main__':
    nums = [1]
    k = 3
    sol = Solution()
    sol.rotate(nums, k)
    print nums

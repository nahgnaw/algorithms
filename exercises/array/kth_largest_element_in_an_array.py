# -*- coding: utf-8 -*-

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution(object):
    # Average O(n). Worst O(n^2)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quick_select(left, right):
            pivot = nums[left]
            lp, rp = left, right
            while lp < rp:
                while nums[rp] <= pivot and lp < rp:
                    rp -= 1
                while nums[lp] >= pivot and lp < rp:
                    lp += 1
                nums[lp], nums[rp] = nums[rp], nums[lp]
            nums[left], nums[lp] = nums[lp], nums[left]
    
            if lp + 1 == k:
                return nums[lp]
            elif lp + 1 > k:
                return quick_select(left, lp - 1)
            else:
                return quick_select(lp + 1, right)
            
        return quick_select(0, len(nums) - 1)

    def findKthSmallest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quick_select(left, right):
            pivot = nums[left]
            lp, rp = left, right
            while lp < rp:
                while nums[rp] >= pivot and lp < rp:
                    rp -= 1
                while nums[lp] <= pivot and lp < rp:
                    lp += 1
                nums[lp], nums[rp] = nums[rp], nums[lp]
            nums[left], nums[lp] = nums[lp], nums[left]
    
            if lp + 1 == k:
                return nums[lp]
            elif lp + 1 > k:
                return quick_select(left, lp - 1)
            else:
                return quick_select(lp + 1, right)
            
        return quick_select(0, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,5,5,1]
    k = 2
    print sol.findKthLargest(nums, k)
    print sol.findKthSmallest(nums, k)
        
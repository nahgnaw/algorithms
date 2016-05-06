# -*- coding -*- 

"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def search_for_left(x):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
            
        def search_for_right(x):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] <= x:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
            
        left, right = search_for_left(target), search_for_right(target)
        return [left, right] if left <= right else [-1, -1]
        


if __name__ == '__main__':
    nums = [4, 7, 7, 8, 8, 10]
    target = 7
    sol = Solution()
    print sol.searchRange(nums, target)

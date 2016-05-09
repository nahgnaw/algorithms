# -*- coding: utf-8 -*-

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        max_sum = cur_sum = nums[0]
        for x in nums[1:]:
            # cur_sum either include x into the previous sum or only contains x.
            cur_sum = max(x, cur_sum + x)
            max_sum = max(max_sum, cur_sum)
        return max_sum

    # Track max subarray indexes.
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None, None, None
    
        max_sum = cur_sum = nums[0]
        max_left = max_right = 0
        cur_left = 0

        for i in xrange(1, len(nums)):
            if cur_sum + nums[i] > nums[i]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
                cur_left = i

            if cur_sum > max_sum:
                max_sum = cur_sum
                max_left = cur_left
                max_right = i

        return max_sum, max_left, max_right


if __name__ == '__main__':
    sol = Solution()
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,-2,-2]
    print sol.maxSubArray2(nums)

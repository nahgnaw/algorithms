# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not len(height):
            return 0
        
        total_volume = last_volume = 0
        stack = []
        i = 0
        while i < len(height):
            if not len(stack) or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                last_ind = stack.pop()
                # A volume is decided by the width and the minimum of its left boundary and right boundary 
                last_volume = 0 if not len(stack) \
                                else (min(height[stack[-1]], height[i]) - height[last_ind]) * (i - stack[-1] - 1)
                total_volume += last_volume
        return total_volume
        
    
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not len(height):
            return 0
        
        l, r = 0, len(height) - 1    
        left_max = right_max = 0
        total_volume = 0
        while l <= r:
            if left_max <= right_max:
                left_max = max(height[l], left_max)
                total_volume += left_max - height[l]
                l += 1
            else:
                right_max = max(height[r], right_max)
                total_volume += right_max - height[r]
                r -= 1
        return total_volume

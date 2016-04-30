# -*- coding: utf-8 -*-

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            # Move the pointer with the smaller height
            # If move the pointer with the bigger height, max_area will definitely not increase
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area

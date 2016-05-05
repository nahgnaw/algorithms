# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        # The first zero is to make sure the stack is not empty so we can start the loop
        # The second zero is used to empty the stack in the end
        heights = [0] + heights + [0]
        # The stack is storing the indcies with increasing bar heights
        stack = [0]
        max_area = 0
        for i in xrange(1, len(heights)):
            # When the current bar (i) is lowerer the last bar in the stack,
            # pop all the bars that is higher than bar i one by one,
            # and compute the areas one by one, keep the maximum one.
            while heights[i] < heights[stack[-1]]:
                ind = stack[-1]
                stack.pop()
                max_area = max(max_area, heights[ind] * (i - stack[-1] - 1))
            stack.append(i)
        return max_area
        
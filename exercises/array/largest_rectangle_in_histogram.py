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
    # O(n^3)
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def get_height(width):
            max_height = 0
            for i in xrange(len(heights)):
                if i + width < len(heights) + 1:
                    max_height = max(max_height, min(heights[i:i+width]))
            return max_height
        
        
        if not heights:
            return 0
          
        max_area = 0  
        for width in xrange(1, len(heights) + 1):
            max_area = max(max_area, width * get_height(width))
        return max_area

    # O(n^2)
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        # Append a zero to the end of heights so that the stack can be emptied in the end.
        heights = heights + [0]
        # The stack is storing the indcies with increasing bar heights.
        stack = [-1]
        max_area = 0
        for i in xrange(len(heights)):
            # If the bar height is increasing, the area must be also
            # increasing, we push the current bar height into the stack.
            # When the current bar (i) is lowerer the last bar in the stack,
            # we don't know if the area will be increased or decreased, so
            # pop all the bars that is higher than bar i one by one,
            # and compute the areas one by one, keep the maximum one.
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
        
# -*- coding: utf-8 -*-

"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
"""


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.larger_half = []   # min heap
        self.smaller_half = []  # max heap
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        from heapq import *
        # Keep larger values in larger_half and smaller values in smaller_half
        heappush(self.smaller_half, -heappushpop(self.larger_half, num))
        if len(self.larger_half) < len(self.smaller_half):
            heappush(self.larger_half, -heappop(self.smaller_half))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # Size of the data is odd
        if len(self.larger_half) > len(self.smaller_half):
            return self.larger_half[0]
        # Size of the data is even
        return (self.larger_half[0] - self.smaller_half[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
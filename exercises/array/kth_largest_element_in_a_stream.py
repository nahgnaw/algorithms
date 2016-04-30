# -*- coding: utf-8 -*-

"""
Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
int findKthLargest() - Return the Kth largest number.
"""


class StreamData(object):

    def __init__(self, k):
        self.heap = []
        self.k = k

    def addNum(self, num):
        import heapq

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        else:
            if num > self.heap[0]:
                heapq.heappushpop(self.heap, num)

    def findKthLargest(self):
        if len(self.heap) < self.k:
            return None
        return self.heap[0]


if __name__ == '__main__':
    sd = StreamData(3)
    sd.addNum(3)
    sd.addNum(6)
    sd.addNum(2)
    sd.addNum(1)
    sd.addNum(10)
    sd.addNum(4)
    sd.addNum(1)
    print sd.findKthLargest()
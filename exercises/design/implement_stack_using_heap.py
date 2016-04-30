# -*- coding: utf-8 -*-

"""
Implement a stack using a heap.
"""

import heapq

class Stack(object):

    def __init__(self):
        self.heap = []
        self.priority = 0

    def push(self, x):
        heapq.heappush(self.heap, (self.priority, x))
        self.priority -= 1

    def pop(self):
        res = heapq.heappop(self.heap)
        self.priority += 1
        return res[1]

    def top(self):
        return self.heap[0][1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack.pop()
    stack.push(4)
    print stack.pop()

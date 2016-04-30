# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    # The actual stored value is x - self.min. 
    # In this way, if a value is less than 0, 
    # it means the actual value is a min. When
    # it is poped, self.min should be updated.
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack:
            return
        
        if self.stack[-1] < 0:
            self.min -= self.stack[-1]
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] + self.min if self.stack[-1] > 0 else self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    print min_stack.top()
    print min_stack.getMin()
    min_stack.pop()
    print min_stack.getMin()
    print min_stack.top()

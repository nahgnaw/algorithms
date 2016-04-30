# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMax() -- Retrieve the maximum element in the stack.
"""

class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = None

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
            self.max = x
        else:
            self.stack.append(x - self.max)
            if x > self.max:
                self.max = x

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack:
            return
        
        if self.stack[-1] > 0:
            self.max -= self.stack[-1]
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] + self.max if self.stack[-1] < 0 else self.max

    def getMax(self):
        """
        :rtype: int
        """
        return self.max


if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(1)
    max_stack.push(-1)
    max_stack.push(2)
    max_stack.push(-2)
    print max_stack.top()
    print max_stack.getMax()
    max_stack.pop()
    print max_stack.getMax()
    print max_stack.top()

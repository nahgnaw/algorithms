# -*- coding: utf8 -*-

from utils import Empty


class LinkedStack:

    class _Node:

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

        @property
        def element(self):
            return self._element

        @property
        def next(self):
            return self._next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._head.element

    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        return e


if __name__ == '__main__':

    s = LinkedStack()

    print 'Empty stack? {}'.format(s.is_empty())

    for i in xrange(5):
        s.push(i)

    print 'Stack length: {}'.format(len(s))
    print 'Stack top: {}'.format(s.top())

    for i in xrange(5):
        print s.pop()

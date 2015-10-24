# -*- coding: utf8 -*-

from utils import Empty


class LinkedQueue:

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

        @next.setter
        def next(self, e):
            self._next = e

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        return self._head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail.next = new
        self._tail = new
        self._size += 1

if __name__ == '__main__':

    q = LinkedQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(5):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()

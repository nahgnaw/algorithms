# -*- coding: utf8 -*-

from utils import Empty


class CircularQueue:

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
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        head = self._tail.next
        return head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next
        self._size -= 1
        return head.element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new.next = new
        else:
            new.next = self._tail.next
            self._tail.next = new
        self._tail = new
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail.next


if __name__ == '__main__':

    q = CircularQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(5):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()


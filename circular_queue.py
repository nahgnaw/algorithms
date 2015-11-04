# -*- coding: utf8 -*-

from utils import Empty


class CircularQueue(object):

    class _Node:

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

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
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


if __name__ == '__main__':

    q = CircularQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(5):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()


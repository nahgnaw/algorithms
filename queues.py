# -*- coding: utf8 -*-

from utils import Empty


class ArrayQueue(object):

    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._arr = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        return self._arr[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        e = self._arr[self._front]
        self._arr[self._front] = None
        self._front = (self._front + 1) % len(self._arr)
        self._size -= 1
        return e

    def enqueue(self, e):
        if self._size == len(self._arr):
            self._resize(2 * len(self._arr))
        end = (self._front + self._size) % len(self._arr)
        self._arr[end] = e
        self._size += 1

    def _resize(self, cap):
        tmp = self._arr
        self._arr = [None] * cap
        walk = self._front
        for k in xrange(self._size):
            self._arr[k] = tmp[walk]
            walk = (walk + 1) % len(tmp)
        self._front = 0
        print 'Resized queue.'


class CircularQueue(object):

    class _Node(object):

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


class LinkedQueue(object):

    class _Node(object):

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

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
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty queue!')
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1


if __name__ == '__main__':

    q = ArrayQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(6):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()

    q = CircularQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(5):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()

    q = LinkedQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(5):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()

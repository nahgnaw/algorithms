# -*- coding: utf8 -*-


class Empty(Exception):
    pass


class ArrayQueue:

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


if __name__ == '__main__':

    q = ArrayQueue()
    print 'Empty queue? {}'.format(q.is_empty())

    for i in xrange(6):
        q.enqueue(i)
    print 'Queue length: {}'.format(len(q))

    for i in xrange(5):
        print q.dequeue()





# -*- coding: utf8 -*-

from utils import Empty


class ArrayStack(object):

    def __init__(self):
        self._arr = []

    def __len__(self):
        return len(self._arr)

    def is_empty(self):
        return len(self._arr) == 0

    def push(self, e):
        self._arr.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._arr[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._arr.pop()


if __name__ == '__main__':

    s = ArrayStack()

    print 'Empty stack? {}'.format(s.is_empty())

    for i in xrange(5):
        s.push(i)

    print 'Stack length: {}'.format(len(s))
    print 'Stack top: {}'.format(s.top())

    for i in xrange(5):
        print s.pop()

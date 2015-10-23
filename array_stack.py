# -*- coding: utf8 -*-


class Empty(Exception):
    pass


class ArrayStack:

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

    print 'Empty stack? {0}'.format(s.is_empty())

    s.push('a')
    s.push('b')
    s.push('c')

    print 'Stack length: {0}'.format(len(s))
    print 'Stack top: {0}'.format(s.top())

    s.pop()
    print 'Stack length: {0}'.format(len(s))

    s.pop()
    print 'Stack length: {0}'.format(len(s))

    s.pop()
    print 'Stack length: {0}'.format(len(s))

    s.pop()
    print 'Stack length: {0}'.format(len(s))

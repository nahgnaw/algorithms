# -*- coding: utf8 -*-

import ctypes


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._arr = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index.')
        return self._arr[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._arr[self._n] = obj
        self._n += 1

    def _resize(self, c):
        new_arr = self._make_array(c)
        for k in xrange(self._n):
            new_arr[k] = self._arr[k]
        self._arr = new_arr
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    @property
    def size(self):
        return arr._n

    @property
    def capacity(self):
        return arr._capacity


if __name__ == '__main__':

    arr = DynamicArray()
    for i in xrange(1000):
        arr.append(i)
        print arr.size, arr.capacity

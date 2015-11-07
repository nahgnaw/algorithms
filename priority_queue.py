# -*- coding: utf8 -*-

from abc import ABCMeta
from positional_list import PositionalList
from utils import Empty


class PriorityQueueBase(object):

    __metaclass__ = ABCMeta

    class _Item(object):

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        min = self._data.first()
        walk = self._data.after(min)
        while walk is not None:
            if walk.element() < min.element():
                min = walk
            walk = self._data.after(min)
        return min

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        new = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_before(walk, new)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return item._key, item._value

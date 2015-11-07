# -*- coding: utf8 -*-

from abc import ABCMeta, abstractmethod


class PriorityQueueBase(object):

    __metaclass__ = ABCMeta

    class Item(object):

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0
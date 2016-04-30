# -*- coding: utf-8 -*-

"""
Implement a hash table with separate chaining.
"""

import random
from collections import MutableMapping


class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.key < other.key

class ItemList(object):

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item.key:
                return item.value
        raise KeyError('Key error: {}'.format(repr(k)))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item.key:
                item.value = v
                return
        self._table.append(Item(k, v))

    def __delitem__(self, k):
        for j in xrange(len(self._table)):
            if k == self._table[j].key:
                self._table.pop(j)
                return
        raise KeyError('Key error: {}'.format(repr(k)))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item.key


class HashTable(object):

    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._size = 0
        self._prime = p
        self._scale = 1 + random.randrange(p - 1)
        self._shift = random.randrange(p)

    """
    Multiply-Add-and-Divide method for compression: [(a * i + b) mod p] mod N
    where N is the size of the bucket array, p is a prime number larger than N, 
    and a and b are integers chosen at random from the interval [0, p − 1], with a > 0.
    """
    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._size

    def __getitem__(self, k):
        j = self._hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error: {}'.format(repr(k)))
        return bucket[k]

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = ItemList()
        old_size = len(self._table[j])
        self._table[j][k] = v
        # If it is not overwriting, table size should increase
        if len(self._table[j]) > old_size:
            self._size += 1
        # Keep load factor <= 0.5
        if self._size > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)  # number 2ˆx - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error: {}'.format(repr(k)))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

    def _resize(self, c):
        old = self._table[:]
        self._table = c * [None]
        self._size = 0
        for item_list in old:
            if item_list is not None:
                for k in item_list:
                    self[k] = item_list[k]


if __name__ == '__main__':
    table = HashTable(2)
    table['a'] = 1
    table['b'] = 2
    for k in table:
        print k, table[k]



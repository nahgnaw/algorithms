# -*- coding: utf-8 -*-

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""


from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dictionary = {}
        self.queue = deque([])
        self.capacity = capacity

    # O(n)
    def get(self, key):
        """
        :rtype: int
        """
        if not key in self.dictionary:
            return -1
            
        self.queue.remove(key)
        self.queue.append(key)
        return self.dictionary[key]

    # O(n)
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dictionary:
            self.queue.remove(key)
        else:
            # If the capacity is met, remove the least recently used item.
            if len(self.dictionary) == self.capacity:
                k = self.queue.popleft()
                self.dictionary.pop(k)
        self.dictionary[key] = value
        self.queue.append(key)
            

class LRUCache2(object):

    class _Node(object):

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None    

    def __init__(self, capacity):
        self.dictionary = {}
        self.capacity = capacity
        self.head = self._Node(0, 0)
        self.tail = self._Node(0, 0)

        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None

    def _delete_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _append_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node

    # O(1)
    def get(self, key):
        if not key in self.dictionary:
            return -1

        node = self.dictionary[key]
        self._delete_node(node)
        self._append_node(node)
        return node.value

    # O(1)
    def set(self, key, value):
        if key in self.dictionary:
            node = self.dictionary[key]
            node.value = value
            self._delete_node(node)
        else:
            node = self._Node(key, value)
            if len(self.dictionary) == self.capacity:
                self.dictionary.pop(self.head.next.key)
                self._delete_node(self.head.next)
            self.dictionary[key] = node
        self._append_node(node)


if __name__ == '__main__':
    capacity = 1
    cache = LRUCache2(capacity)
    cache.set(2, 1)
    print cache.get(2)
    cache.set(3, 2)

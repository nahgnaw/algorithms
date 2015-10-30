# -*- coding: utf8 -*-

from abc import ABCMeta, abstractmethod


class Tree(object):

    __metaclass__ = ABCMeta

    class Position(object):

        @abstractmethod
        def element(self):
            return

        @abstractmethod
        def __eq__(self, other):
            return

        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def root(self):
        return

    @abstractmethod
    def parent(self, p):
        return

    @abstractmethod
    def num_children(self, p):
        return

    @abstractmethod
    def children(self, p):
        return

    @abstractmethod
    def __len__(self):
        return

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(parent) for parent in self.children(p))

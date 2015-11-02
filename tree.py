# -*- coding: utf8 -*-

from abc import ABCMeta, abstractmethod
from linked_queue import LinkedQueue


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

    def __iter__(self):
        for p in self.positions():
            yield p.element()

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
        yield

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

    def positions(self):
        return self.preorder()

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def breadth_first(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def preorder_label(self, p, d, path):
        label = '.'.join(str(i+1) for i in path)
        print 2 * d * ' ' + label, str(p.element())
        path.append(0)
        for c in self.children(p):
            self.preorder_label(c, d+1, path)
            path[-1] += 1
        path.pop()

    def parenthesize(self, p):
        print p.element(),
        if not self.is_leaf(p):
            first_time = True
            for c in self.children(p):
                sep = ' (' if first_time else ' ,'
                print sep,
                first_time = False
                self.parenthesize(c)
            print ')',


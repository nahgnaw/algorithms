# -*- coding: utf8 -*-

from tree import ABCMeta, abstractmethod, Tree


class BinaryTree(Tree):

    __metaclass__ = ABCMeta

    @abstractmethod
    def left(self, p):
        return

    @abstractmethod
    def right(self, p):
        return

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
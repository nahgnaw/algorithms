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

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def positions(self):
        return self.inorder()

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

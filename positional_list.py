# -*- coding: utf8 -*-

from doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super(PositionalList, self)._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def insertion_sort(self):
        if len(self) > 1:
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)

    def print_list(self):
        l = []
        for k in self:
            l.append(str(k))
        return ' '.join(l)


if __name__ == '__main__':

    pl = PositionalList()

    pl.add_first(100)
    pl.add_last(1)

    print 'Current list: {}'.format(pl.print_list())

    for i in xrange(20):
        pl.add_first(i)
    print 'Current list: {}'.format(pl.print_list())

    pl.insertion_sort()
    print 'Current list: {}'.format(pl.print_list())

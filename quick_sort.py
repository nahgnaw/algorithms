# -*- coding: utf8 -*-

from queues import LinkedQueue


def quick_sort(s):
    n = len(s)
    if n < 2:
        return
    p = s.first()
    less = LinkedQueue()
    equal = LinkedQueue()
    greater = LinkedQueue()
    while not s.is_empty():
        if s.first() < p:
            less.enqueue(s.dequeue())
        elif p < s.first():
            greater.enqueue(s.dequeue())
        else:
            equal.enqueue(s.dequeue())
    quick_sort(less)
    quick_sort(greater)
    while not less.is_empty():
        s.enqueue(less.dequeue())
    while not equal.is_empty():
        s.enqueue(equal.dequeue())
    while not greater.is_empty():
        s.enqueue(greater.dequeue())


if __name__ == '__main__':

    s = LinkedQueue()
    for i in xrange(10):
        s.enqueue(10 - i)
    quick_sort(s)
    for i in xrange(10):
        print s.dequeue()

# -*- coding: utf8 -*-

import math
import random
import copy
import time


def bubble_sort(s):
    for i in xrange(len(s)):
        for j in xrange(len(s) - 1 - i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]


def insertion_sort(s):
    for i in xrange(1, len(s)):
        j = i
        while j > 0 and s[j] < s[j-1]:
            s[j], s[j-1] = s[j-1], s[j]
            j -= 1


def merge_sort(s):

    def merge(l, r, s):
        i = j = 0
        while i + j < len(s):
            if j == len(r) or (i < len(l) and l[i] < r[j]):
                s[i+j] = l[i]
                i += 1
            else:
                s[i+j] = r[j]
                j += 1

    n = len(s)
    if n < 2:
        return
    mid = n // 2
    l = s[0:mid]
    r = s[mid:n]
    merge_sort(l)
    merge_sort(r)
    merge(l, r, s)


def nonrecursive_merge_sort(s):

    def merge(src, result, start, inc):
        end_1 = start + inc
        end_2 = min(start + 2 * inc, len(src))
        x, y, z = start, start + inc, start
        while x < end_1 and y < end_2:
            if src[x] < src[y]:
                result[z] = src[x]
                x += 1
            else:
                result[z] = src[y]
                y += 1
            z += 1
        if x < end_1:
            result[z:end_2] = src[x:end_1]
        elif y < end_2:
            result[z:end_2] = src[y:end_2]

    n = len(s)
    if n < 2:
        return
    logn = int(math.ceil(math.log(n, 2)))
    src, dest = s, [None] * n
    for i in (2 ** k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n]





if __name__ == '__main__':

    numbers = [random.randint(-50, 100) for c in range(32)]
    print 'Original: {}\n'.format(' '.join(str(x) for x in numbers))

    numbers_copy = copy.deepcopy(numbers)
    ts = time.time()
    bubble_sort(numbers_copy)
    te = time.time()
    print 'Bubble sort: {}'.format(' '.join(str(x) for x in numbers_copy))
    print '{:.4e}\n'.format(te - ts)

    numbers_copy = copy.deepcopy(numbers)
    ts = time.time()
    insertion_sort(numbers_copy)
    te = time.time()
    print 'Insertion sort: {}'.format(' '.join(str(x) for x in numbers_copy))
    print '{:.4e}\n'.format(te - ts)

    numbers_copy = copy.deepcopy(numbers)
    ts = time.time()
    merge_sort(numbers_copy)
    te = time.time()
    print 'Merge sort (recursive): {}'.format(' '.join(str(x) for x in numbers_copy))
    print '{:.4e}\n'.format(te - ts)

    numbers_copy = copy.deepcopy(numbers)
    ts = time.time()
    nonrecursive_merge_sort(numbers_copy)
    te = time.time()
    print 'Merge sort (non-recursive): {}'.format(' '.join(str(x) for x in numbers_copy))
    print '{:.4e}\n'.format(te - ts)

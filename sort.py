# -*- coding: utf8 -*-

import math
import random
import copy
import time


# Time: O(n^2). Space: O(1). Stable.
def bubble_sort(items):
    for i in xrange(len(items)):
        for j in xrange(len(items) - 1 - i):
            if items[j] > items[j+1]:
                items[j], items[j + 1] = items[j + 1], items[j]


# Time: O(n^2). Space: O(1). Unstable.
def selection_sort(items):
    for i in xrange(len(items)):
        min = i
        for j in xrange(i + 1, len(items)):
            if items[j] < items[min]:
                min = j
        items[i], items[min] = items[min], items[i]


# Time: O(n^2). Space: O(1). Stable.
def insertion_sort(items):
    for i in xrange(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1


# Time: O(nlogn). Space: O(1). Stable.
def merge_sort(items):

    def merge(l, r, s):
        i = j = 0
        while i + j < len(s):
            if j == len(r) or (i < len(l) and l[i] < r[j]):
                s[i+j] = l[i]
                i += 1
            else:
                s[i+j] = r[j]
                j += 1

    n = len(items)
    if n < 2:
        return
    mid = n // 2
    left = items[0:mid]
    right = items[mid:n]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, items)


def nonrecursive_merge_sort(items):

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

    n = len(items)
    logn = int(math.ceil(math.log(n, 2)))
    src, dest = items, [None] * n
    for i in (2 ** k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if items is not src:
        items[0:n] = src[0:n]


# Time: O(nlogn). Space: O(1). Unstable.
def quick_sort(items, left, right):
    if left >= right:
        return items

    marker = items[left]
    lp, rp = left, right
    while lp < rp:
        while items[rp] >= marker and lp < rp:
            rp -= 1
        while items[lp] <= marker and lp < rp:
            lp += 1
        items[lp], items[rp] = items[rp], items[lp]
    items[left], items[lp] = items[lp], items[left]

    quick_sort(items, left, lp - 1)
    quick_sort(items, rp + 1, right)



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
    selection_sort(numbers_copy)
    te = time.time()
    print 'selection sort: {}'.format(' '.join(str(x) for x in numbers_copy))
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

    numbers_copy = copy.deepcopy(numbers)
    ts = time.time()
    quick_sort(numbers_copy, 0, len(numbers_copy) - 1)
    te = time.time()
    print 'Quick sort: {}'.format(' '.join(str(x) for x in numbers_copy))
    print '{:.4e}\n'.format(te - ts)

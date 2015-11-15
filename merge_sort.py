# -*- coding: utf8 -*-

import math


def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s_1 = s[0:mid]
    s_2 = s[mid:n]
    merge_sort(s_1)
    merge_sort(s_2)
    merge(s_1, s_2, s)


def merge(s_1, s_2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s_2) or (i < len(s_1) and s_1[i] < s_2[j]):
            s[i+j] = s_1[i]
            i += 1
        else:
            s[i+j] = s_2[j]
            j += 1


def nonrecursive_merge_sort(s):
    n = len(s)
    if n < 2:
        return
    logn = int(math.ceil(math.log(n, 2)))
    src, dest = s, [None] * n
    for i in (2 ** k for k in range(logn)):
        for j in range(0, n, 2*i):
            nonrecursive_merge(src, dest, j, i)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n]


def nonrecursive_merge(src, result, start, inc):
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


if __name__ == '__main__':

    s = [4, 9, 1, 6, 5, 8, 7, 3, 2, 0]
    merge_sort(s)
    print s
    nonrecursive_merge_sort(s)
    print s

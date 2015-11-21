# -*- coding: utf8 -*-


def brute_force(string, pattern):
    n, m = len(string), len(pattern)
    for i in xrange(n - m + 1):
        k = 0
        while k < m and string[i+k] == pattern[k]:
            k += 1
        if k == m:
            return i
    return -1


def boyer_moore(string, pattern):
    n, m = len(string), len(pattern)
    if m == 0:
        return 0
    last = {}
    for k in xrange(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if string[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(string[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1


def kmp(string, pattern):

    def compute_fail(pattern):
        m = len(pattern)
        fail = [0] * m
        j = 1
        k = 0
        while j < m:
            if pattern[j] == pattern[k]:
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k-1]
            else:
                j += 1
        return fail

    n, m = len(string), len(pattern)
    if m == 0:
        return 0
    fail = compute_fail(pattern)
    j = 0
    k = 0
    while j < n:
        if string[j] == pattern[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


if __name__ == '__main__':
    string = u'abcdefghijklmnopqrstuvwxyz'
    pattern = u'opqrst'
    print brute_force(string, pattern)
    print boyer_moore(string, pattern)
    print kmp(string, pattern)

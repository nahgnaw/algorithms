# -*- coding: utf8 -*-


def lcs(x, y):
    n, m = len(x), len(y)
    l = [[0] * (m + 1) for k in xrange(n + 1)]
    for j in xrange(n):
        for k in xrange(m):
            if x[j] == y[k]:
                l[j+1][k+1] = l[j][k] + 1
            else:
                l[j+1][k+1] = max(l[j][k+1], l[j+1][k])
    return l


def lcs_solution(l, x, y):
    solution = []
    j, k = len(x), len(y)
    while l[j][k] > 0:
        if x[j-1] == y[k-1]:
            solution.append(x[j-1])
            j -= 1
            k -= 1
        elif l[j-1][k] >= l[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))


if __name__ == '__main__':
    x = 'GTTCCTAATA'
    y = 'CGATAATTGAGA'
    l = lcs(x, y)
    print lcs_solution(l, x, y)

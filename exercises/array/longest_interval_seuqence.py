# -*- coding: utf-8 -*-

"""
Given a set of [a,b] intervals on the number line, find the longest ordered sequence (consecutive in original order) of (a subset of) the intervals such that each consecutive interval is nested inside the previous one.
"Nested" means this: If interval X is nested inside Y, then Y.a < X.a and X.b < Y.b.

E.g. given [[3,4], [1,9], [2,8], [4,5], [11,12]]
Return: [[1, 9], [2, 8], [4, 5]]
"""


class Solution(object):
    def inteval_sequence(self, intervals):
        if not intervals:
            return []

        result, tmp = [], []
        max_len = 0
        for i in xrange(len(intervals) - 1):
            tmp.append(intervals[i])
            if intervals[i+1][0] <= intervals[i][0] or intervals[i+1][1] >= intervals[i][1]:
                if len(tmp) > max_len:
                    max_len = len(tmp)
                    result = tmp[:]
                tmp = []
        return result


if __name__ == '__main__':
    sol = Solution()
    intervals = [[0,7], [1,9], [2,8], [4,5], [11,12]]
    print sol.inteval_sequence(intervals)
            
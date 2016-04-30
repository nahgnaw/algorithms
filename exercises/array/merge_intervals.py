# -*- coding: utf-8 -*-

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
            
        res = []
        for i in intervals.sort(key=lambda x: x.start):
            if res and res[-1].end >= i.start:
                res[-1].start, res[-1].end = min(res[-1].start, i.start), max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
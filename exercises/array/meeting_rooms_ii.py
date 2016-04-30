# -*- coding: utf-8 -*-

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
            
        import heapq
        
        intervals.sort(key=lambda x: x.start)
        end_times = []  # A min heap.
        for i in intervals:
            # If the next meeting starts no earlier than 
            # the current meeting's ending time, we don't 
            # need a new room. 
            if end_times and i.start >= end_times[0]:
                heapq.heapreplace(end_times, i.end)
            # Else we'll need a new room.
            else:
                heapq.heappush(end_times, i.end)
        return len(end_times)

    def minMeetingRooms2(self, intervals):
        start_times, end_times = [], []
        for i in intervals:
            start_times.append(i.start)
            end_times.append(i.end)
        start_times.sort()
        end_times.sort()

        s = e = 0
        rooms_needed = rooms_available = 0
        while s < len(start_times):
            if start_times[s] < end_times[e]:
                if not rooms_available:
                    rooms_needed += 1
                else:
                    rooms_available -= 1
                s += 1
            else:
                rooms_available += 1
                e += 1

        return rooms_needed
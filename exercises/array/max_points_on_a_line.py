# -*- coding: utf-8 -*-

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        
        result = 0
        for i in xrange(len(points)):
            # Store counts of slopes in a dictionary.
            d = {}
            cur_max, overlapping = 0, 0
            for j in xrange(i + 1, len(points)):
                dx, dy = points[j].x - points[i].x, points[j].y - points[i].y
                # Count overlapping points
                if dx == 0 and dy == 0:
                    overlapping += 1
                    continue
                slope = float(dy) / dx if not dx == 0 else 'inf'
                d[slope] = d.setdefault(slope, 0) + 1
                cur_max = max(cur_max, d[slope])
            result = max(result, cur_max + overlapping + 1)
        return result
                
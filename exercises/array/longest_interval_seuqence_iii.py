# -*- coding: utf-8 -*-

"""
Given a set of [a,b] intervals on the number line, find the longest sequence of (a subset of) the intervals such that each consecutive interval is nested inside the previous one.
"Nested" means this: If interval X is nested inside Y, then Y.a < X.a and X.b < Y.b.

Note: the original order doesn't need to be maintained.
    
E.g. given [[1,10], [3,4], [4,5], [11,12], [3,8], [2,9]]
Return: [[1,10], [2,9], [3,8], [4,5]]

sort by left value
dp[i]: number of longest sequence
dp[i] = max([dp[j] + 1 for j in xrange(i) if i is nested in j])
"""

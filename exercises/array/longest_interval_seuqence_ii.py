# -*- coding: utf-8 -*-

"""
Given a set of [a,b] intervals on the number line, find the longest ordered sequence of (a subset of) the intervals such that each consecutive interval is nested inside the previous one.
"Nested" means this: If interval X is nested inside Y, then Y.a < X.a and X.b < Y.b.
    
E.g. given [[1,10], [3,4], [2,9], [3,8], [4,5], [11,12]]
Return: [[1,10], [2,9], [3,8], [4,5]]
"""


class Solution(object):
    def interval_sequence(self, intervals):
        if not intervals:
            return []

        # dp[i]: the number of longest ordered interval sequence that ends with intervals[i]
        dp = [1] * len(intervals)
        # Record the longest ordered interval sequence for each interval
        sequences = [[intervals[i]] for i in xrange(len(intervals))]
        for i in xrange(1, len(intervals)):
            max_seq_len = 0
            tmp_seq = []
            # Look at every previous interval j of i, check if i is nested in j
            # If i is nested in j, dp[i] == max(dp[j]) + 1
            for j in xrange(i):
                if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                    if dp[j] + 1 > max_seq_len:
                        max_seq_len = dp[j] + 1
                        tmp_seq = sequences[j] + [intervals[i]]
            # If i is nested in none of its previous intervals, dp[i] = 1
            if max_seq_len > 1:
                dp[i] = max_seq_len
                sequences[i] = tmp_seq[:]

        # Return the longest one in sequences.
        result = sequences[0]
        for seq in sequences[1:]:
            if len(seq) > len(result):
                result = seq[:]
        return result


if __name__ == '__main__':
    sol = Solution()
    intervals = [[3,10], [3,4], [1,9], [3,8], [4,5], [11,12]]
    print sol.interval_sequence(intervals)

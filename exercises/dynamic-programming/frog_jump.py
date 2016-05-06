# -*- coding: utf-8 -*-

"""
A small frog wants to get to the other side of a pond. The frog is initially located on one bank of the pond (position 0) and wants to get to the other bank (position X). The frog can jump any (integer) distance between 1 and D. If X > D then the frog cannot jump right across the pond. Luckily, there are leaves falling from a tree onto the surface of the pond, and the frog can jump onto and from the leaves.
You are given a zero-indexed array A consisting of N integers. This array represents falling leaves. Initially there are no leaves. A[K] represents the position where a leaf will fall in second K.
The goal is to find the earliest time when the frog can get to the other side of the pond. The frog can jump from and to positions 0 and X (the banks of the pond) and every position with a leaf.
For example, you are given integers X = 7, D = 3 and array A such that:
A[0] = 1
A[1] = 3
A[2] = 1 
A[3] = 4
A[4] = 2
A[5] = 5
Initially, the frog cannot jump across the pond in a single jump. However, in second 3, after a leaf falls at position 4, it becomes possible for the frog to cross. This is the earliest moment when the frog can jump across the pond (by jumps of length 1. 3 and 3).
Write a function:
clan= Solution { public int solution(int[] A, int X, int 0); }
that, given a zero-indexed array A consisting of N integers, and integers X and D, returns the earliest time when the frog can jump to the other side of the pond. If the frog can leap across the pond in just one jump, the function should return 0. If the frog is never able to jump to the other side of the pond, the function should return —1.
For example, given X = 7, D = 3 and array A such that:
A[0] = 1
A[1] = 3
A[2] = 1 
A[3] = 4
A[4] = 2
A[5] = 5
the function should return 3 as explained above. Assume that:
•   N is an integer within the range [0..100,000];
•   X and D are integers within the range [1..100.000];
•   each element of array A is an integer within the range [1..X-1].
Complexity:
expected worst-case time complexity is 0(N);
expected worst-case space complexity is 0(X), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""


def solution(A, X, D):
    # the frog can leap across the pond in one jump
    if D >= X:
        return 0
        
    # compute the earliest leaf falling time at each position
    # leaf_falling_time[i]: the earliest time for a leaf to fall at position i
    leaf_falling_time = [float('inf')] * (X + 1)    # initialization with infinity meaning no leaf falling here
    leaf_falling_time[0] = leaf_falling_time[-1] = 0    # the two banks
    for i in xrange(len(A)):
        if A[i] < X:
            # if there is no leaf at position i or the current time is greater, assign a new falling time
            if leaf_falling_time[A[i]] == float('inf') or leaf_falling_time[A[i]] > i:
                leaf_falling_time[A[i]] = i
                                
    # compute the earliest time the frog can arrive at each position
    # arrival_time[i]: the earliest time the frog can arrive at position i
    arrival_time = [float('inf')] * (X + 1)     # initialization with infinity meaning the frog can never get here
    arrival_time[0] = 0  # the frog is already at the bank
    for i in xrange(1, X + 1):
        # arrival_time[i] depends on leaf_falling_time[i] and the leaf falling time within the last D positions
        # arrival_time[i] = max(leaf_falling_time[i], min(leaf_falling_time[i-1:i-D]))
        earliest = float('inf')
        for j in xrange(1, D + 1):
            if i - j >= 0:
                earliest = min(earliest, leaf_falling_time[i-j])
        arrival_time[i] = max(earliest, leaf_falling_time[i])
        
    return arrival_time[-1] if not arrival_time[-1] == float('inf') else -1


A = [1,3,1,4,2,5]
X, D = 7, 3
print solution(A, X, D)

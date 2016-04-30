# -*- coding: utf-8 -*-

"""
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity

Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
"""


class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        def _heapify(k):
            n = len(A)
            while k < n:
                min_index = k
                if 2 * k + 1 < n and A[2*k+1] < A[min_index]:
                    min_index = 2 * k + 1
                if 2 * k + 2 < n and A[2*k+2] < A[min_index]:
                    min_index = 2 * k + 2
                if k == min_index:
                    break

                A[k], A[min_index] = A[min_index], A[k]
                k = min_index


        for i in xrange(len(A) / 2, -1, -1):
            _heapify(i)
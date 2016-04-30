# -*- coding: utf-8 -*-

"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
"""


class Solution(object):
    # Sort citations first. O(nlogn)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i in xrange(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0

    def hIndex2(self, citations):
        # O(n). Two passes.
        n = len(citations)
        # nums[i]: the number of papers that have at least i citations
        nums = [0] * (n+1)

        for i in citations:
            if i > n:
                nums[n] += 1
            else:
                nums[i] += 1

        # h-index can be at most n
        if nums[n] >= n:
            return n

        for i in xrange(n-1, -1, -1):
            nums[i] += nums[i+1]
            if nums[i] >= i:
                return i

        return 0
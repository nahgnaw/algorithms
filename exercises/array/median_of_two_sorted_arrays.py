# -*- coding: utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution(object):
    # O(log(m+n))
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def get_kth_smallest(start1, len1, start2, len2, k):
            # If one of the arrays is empty, return kth from the other array.
            if start1 >= len1:
                return nums2[start2+k-1]
            if start2 >= len2:
                return nums1[start1+k-1]
            # If asked for the smallest value, return the smaller one between
            # the first elements of the two arrays.
            if k == 1:
                return min(nums1[start1], nums2[start2])
                
            # Search for the (k/2)th smallest value in each array.
            i, j = min(len1, k / 2), min(len2, k / 2)
            if nums1[start1+i-1] < nums2[start2+j-1]:
                # Discard the smaller half of nums1.
                return get_kth_smallest(start1 + i, len1, start2, len2, k - i)
            else:
                # Discard the smaller half of nums2.
                return get_kth_smallest(start1, len1, start2 + j, len2, k - j)
                
        m, n = len(nums1), len(nums2)
        if (m + n) % 2:
            return get_kth_smallest(0, m, 0, n, (m + n) / 2 + 1)
        return (get_kth_smallest(0, m, 0, n, (m + n) / 2) + \
                get_kth_smallest(0, m, 0, n, (m + n) / 2 + 1)) / 2.0
                
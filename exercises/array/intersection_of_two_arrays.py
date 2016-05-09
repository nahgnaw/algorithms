# -*- coding: utf-8 -*-

"""
Find the intersection of two unsorted arrays.

Follow-up #1: the two arrays are sorted.
Follow-up #2: the two arrays are sorted and array #1 is much larger than array #2.
"""


class Solution(object):
    # O(n). Used for unsorted arrays.
    def intersection(self, arr1, arr2):
        if not arr1 or not arr2:
            return []

        s = set()
        for x in arr1:
            s.add(x)

        results = set()
        for x in arr2:
            if x in s:
                results.add(x)
        return list(results)


    # O(nlogn)
    def intersection2(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if not arr1 or not arr2:
            return []

        arr1.sort()
        arr2.sort()

        results = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            while i > 0 and arr1[i] == arr1[i-1]:
                i += 1
            while j > 0 and arr2[j] == arr2[j-1]:
                j += 1
            if arr1[i] == arr2[j]:
                results.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else: 
                j+= 1
        return results


    # Search every element of smaller array in the larger array.
    # Used when array sizes significantly differ.
    def intersection3(self, arr1, arr2):

        def binary_search(target, arr, left, right):
            if left > right:
                return -1

            while left <= right:
                mid = (left + right) / 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1


        if len(arr1) < len(arr2):
            self.intersection3(arr2, arr1)

        if not arr1 or not arr2:
            return []

        arr1.sort()
        arr2.sort()

        results = set()
        left, right = 0, len(arr1) - 1
        for x in arr2:
            ind = binary_search(x, arr1, left, right)
            if not ind == -1:
                results.add(x)
                left = ind + 1
        return list(results)


if __name__ == '__main__':
    arr1 = [1,3,4,5,5,7]
    arr2 = [6,8,12]
    sol = Solution()
    print sol.intersection(arr1, arr2)
    print sol.intersection2(arr1, arr2)
    print sol.intersection3(arr1, arr2)


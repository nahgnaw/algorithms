# -*- coding: utf-8 -*-

"""
Find common elements in two arrays.
"""


class Solution(object):
    # O(nlogn)
    def commonElements(self, arr1, arr2):
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

    # O(n)
    def commonElements2(self, arr1, arr2):
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


if __name__ == '__main__':
    arr1 = [1,3,4,5,5,7]
    arr2 = [4,5,8,12]
    sol = Solution()
    print sol.commonElements(arr1, arr2)
    print sol.commonElements2(arr1, arr2)

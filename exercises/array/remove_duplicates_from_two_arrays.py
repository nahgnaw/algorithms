# -*- coding: utf-8 -*-

"""
Merge two arrays and remove duplicates.
"""


class Solution(object):
    def remove_dup(self, arr1, arr2):
        arr1.sort()
        arr2.sort()

        result = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            # Skip duplicates in arr1.
            while i < len(arr1) - 1:
                if arr1[i] == arr1[i+1]:
                    i += 1
                else:
                    break
            # Skip duplicates in arr2.
            while j < len(arr2) - 1:
                if arr2[j] == arr2[j+1]:
                    j += 1
                else:
                    break
            # Merge arr1 and arr2.
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        # Include remaining elements in arr1 if any.
        while i < len(arr1):
            while i < len(arr1) - 1:
                if arr1[i] == arr1[i+1]:
                    i += 1
                else:
                    break
            result.append(arr1[i])
            i += 1
        # Include remaining elements in arr2 if any.
        while j < len(arr2):
            while j < len(arr2) - 1:
                if arr2[j] == arr2[j+1]:
                    j += 1
                else:
                    break
            result.append(arr2[j])
            j += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    arr1 = [1,1,1]
    arr2 = [2,2,1]
    print sol.remove_dup(arr1, arr2)

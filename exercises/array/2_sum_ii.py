# -*- coding: utf-8 -*-

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    # Two pointers. O(n).
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return [0, 0]

    # Binary search. O(nlogn).
    def twoSum2(self, numbers, target):
        for i in xrange(len(numbers)):
            diff = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if diff == numbers[mid]:
                    return [i + 1, mid + 1]
                elif diff > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return [0, 0]

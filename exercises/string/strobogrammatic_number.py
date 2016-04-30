# -*- coding: utf-8 -*-

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        table = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        if not num:
            return False

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] in table and table[num[left]] == num[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
# -*- coding: utf-8 -*-

"""
Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.

You code should also return the new length of the string after replacement.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python，please use characters array instead of string.

Challenge
Do it in-place.
"""


class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        if not string:
            return 0 
        
        # Get the count of spaces
        space_count = 0
        for c in string:
            if c == ' ':
                space_count += 1
        new_length = length + 2 * space_count

        # Start from the end of the string, replace spaces
        new = new_length - 1
        for i in xrange(length - 1, -1 , -1):
            if not string[i] == ' ':
                string[new] = string[i]
                new -= 1
            else:
                string[new] = '0'
                new -= 1
                string[new] = '2'
                new -= 1
                string[new] = '%'
                new -= 1

        return new_length


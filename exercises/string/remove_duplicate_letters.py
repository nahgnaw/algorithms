# -*- coding: utf-8 -*-

"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_char_index(c):
            return ord(c) - ord('a')

        occurences = [0] * 26
        visited = [False] * 26

        # Character occurrences
        for c in s:
            occurences[get_char_index(c)] += 1

        result = []
        for c in s:
            # Decrease character occurrence
            index = get_char_index(c)
            occurences[index] -= 1

            if visited[index]:
                continue

            # If result[-1] is larger than c and it will appear later, remove it for now
            while result and ord(result[-1]) > ord(c) and occurences[get_char_index(result[-1])]:
                last = result.pop()
                visited[get_char_index(last)] = False
            result.append(c)
            visited[get_char_index(c)] = True

        return ''.join(result)



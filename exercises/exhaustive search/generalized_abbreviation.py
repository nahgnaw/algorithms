# -*- coding: utf-8 -*-

"""
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        self._generateAbbreviations(result, word, 0, '', 0)
        return result

    def _generateAbbreviations(self, result, word, pos, temp, number_count):
        if pos == len(word):
            if number_count:
                temp += str(number_count)
            result.append(temp)
        else:
            # For every character, it can be either abbreviated or not.
            # If a character is abbreviated, do not include it in temp and increase number_count (because it'll be replaced by a number)
            self._generateAbbreviations(result, word, pos + 1, temp, number_count + 1)
            # If a character is not abbreviated, append current number_count to temp and then append the character to temp
            self._generateAbbreviations(result, word, pos + 1, temp + (str(number_count) if number_count else '') + word[pos], 0)

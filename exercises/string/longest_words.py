# -*- coding: utf-8 -*-

"""
Given a dictionary, find all of the longest words in the dictionary.

Example
Given

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
the longest words are(is) ["internationalization"].

Given

{
  "like",
  "love",
  "hate",
  "yes"
}
the longest words are ["like", "love", "hate"].

Challenge
It's easy to solve it in two passes, can you do it in one pass?
"""


class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        result = []
        max_len = 0
        for word in dictionary:
            if len(word) > max_len:
                max_len = len(word)
                result[:] = []
                result.append(word)
            elif len(word) == max_len:
                result.append(word)
        return result
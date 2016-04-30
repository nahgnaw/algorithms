# -*- coding: utf-8 -*-

"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = {}
        for w in dictionary:
            if len(w) > 2:
                abbr = w[0] + str(len(w)) + w[-1]
                self.abbrs.setdefault(abbr, set()).add(w)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if not self.abbrs or not word:
            return True
            
        word_len = len(word)
        if word_len <= 2:
            return False

        abbr = word[0] + str(word_len) + word[-1]
        if abbr not in self.abbrs:
            return True
        elif word in self.abbrs[abbr] and len(self.abbrs[abbr]) == 1:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
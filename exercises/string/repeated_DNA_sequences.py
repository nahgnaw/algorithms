# -*- coding: utf-8 -*-

"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
          
        counts = {}
        for i in xrange(len(s)):
            if i + 10 <= len(s):
                seq = s[i:i+10]
                counts[seq] = counts.setdefault(seq, 0) + 1
                
        result = []
        for seq in counts:
            if counts[seq] > 1:
                result.append(seq)
        return result

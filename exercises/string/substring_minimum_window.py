# -*- coding: utf-8 -*-

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''

        # A dictionary recording characters' frequencies in t.
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.setdefault(c, 0) + 1

        min_win_start, min_win_len = 0, float('inf')
        t_covered_char = 0      # counter for covered characters in t
        start = end = 0     # window boundaries
        while end < len(s):
            # Increase the end pointer to cover all characters in t
            c = s[end]
            if c in t_freq:
                t_freq[c] -= 1
                if t_freq[c] >= 0:
                    t_covered_char += 1

            # When all characters in t are covered, a window is found
            # Now increase the start pointer, trying to decrease the length of this window
            # If the window cannot be smaller any more, search for another window
            while t_covered_char == len(t):
                if end - start + 1 < min_win_len:
                    min_win_len = end - start + 1
                    min_win_start = start

                ch = s[start]
                if ch in t_freq:
                    t_freq[ch] += 1
                    if t_freq[ch] > 0:
                        t_covered_char -= 1
                start += 1

            end += 1

        if min_win_len == float('inf'):
            return ''
        return s[min_win_start:min_win_start+min_win_len]

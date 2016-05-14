# -*- coding: utf-8 -*-

"""
Given a string, find its first non-repeating character.
"""


class Solution(object):
    def first_non_repeating_char(self, s):
        if not s:
            return None

        counts = {}
        for i in xrange(len(s)):
            if s[i] not in counts:
                counts[s[i]] = [1, i]
            else:
                counts[s[i]][0] += 1

        first_ind = len(s)
        for c in counts:
            if counts[c][0] == 1:
                first_ind = min(first_ind, counts[c][1])

        return s[first_ind] if first_ind < len(s) else None


if __name__ == '__main__':
    sol = Solution()
    s = 'abbbcccddde'
    print sol.first_non_repeating_char(s)

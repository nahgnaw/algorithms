# -*- coding: utf-8 -*-

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, 312211, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        results = ['1']
        for k in xrange(1, n):
            cur = ''
            prev = results[k-1]
            i = 0
            while i < len(prev):
                j = i
                while j < len(prev) - 1:
                    if prev[j+1] == prev[j]:
                        j += 1
                    else:
                        break
                count = j - i + 1
                cur += str(count) + str(prev[i])
                i = j + 1
            results.append(cur)
        return results[-1]


if __name__ == '__main__':
    n = 6
    sol = Solution()
    print sol.countAndSay(n)


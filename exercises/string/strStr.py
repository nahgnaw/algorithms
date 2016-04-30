# -*- coding: utf-8 -*- 

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):
    # O(mn)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            for j in xrange(len(needle)):
                if not needle[j] == haystack[i+j]:
                    break
            # If no break happens in the last for loop, execute this else statement. 
            else:
                return i
        return -1


if __name__ == '__main__':
    haystack = 'asdfsdf'
    needle = 'fsd'
    sol = Solution()
    print sol.strStr(haystack, needle)

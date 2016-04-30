"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""

"""
A palindrome can be formed if the number of odd characters is at most 1.
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1

        odd_char = 0
        for k in d:
            if d[k] % 2 == 1:
                odd_char += 1

        return odd_char < 2

    def canPermutePalindrome2(self, s):
        from collections import Counter
        return len(filter(lambda item: item[1] % 2, Counter(s).items())) < 2


if __name__ == '__main__':
    s = 'carerac'
    sol = Solution()
    print sol.canPermutePalindrome(s)
    print sol.canPermutePalindrome2(s)

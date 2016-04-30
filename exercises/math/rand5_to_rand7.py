# -*- coding: utf-8 -*-

"""
Given a function which produces a random integer in the range 1 to 5, write a function which produces a random integer in the range 1 to 7.
"""


class Solution(object):

    def rand5(self):
        import random
        return random.randint(1, 5)

    def rand7(self):
        while True:
            r = 5 * (self.rand5() - 1) + self.rand5()
            #r is now uniformly random between 1 and 25
            if (r <= 21):
                break
        #result is now uniformly random between 1 and 7
        return r % 7 + 1


if __name__ == '__main__':
    sol = Solution()
    distributions = [0] * 8
    for i in xrange(1000000):
        r = sol.rand7()
        distributions[r] += 1
    print distributions

# -*- coding: utf-8 -*-

"""
Design a prime number generator.


The Sieve of Eratosthenes:

Make a list of all the integers less than or equal to n (and greater than one). Strike out the multiples of all primes less than or equal to the square root of n, then the numbers that are left are the primes.

For example, to find all the primes less than or equal to 30, first list the numbers from 2 to 30.
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

The first number 2 is prime, so keep it (we will color it green) and cross out its multiples (we will color them red), so the red numbers are not prime.
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

The first number left (still black) is 3, so it is the first odd prime. Keep it and cross out all of its multiples. We know that all multiples less than 9 (i.e. 6) will already have been crossed out, so we can start crossing out at 32=9.
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

Now the first number left (still black) is 5, the second odd prime. So keep it also and cross out all of its multiples (all multiples less than 52=25 have already been crossed out, and in fact 25 is the only multiple not yet crossed out).
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

The next number left, 7, is larger than the square root of 30, so there are no multiples of 7 to cross off that haven't already been crossed off (14 and 28 by 2, and 21 by 3), and therefore the sieve is complete. Therefore all of the numbers left are primes: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}. Notice we just found these primes without dividing.
"""


class Solution(object):
    def prime_generator(self, n):
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        D = {}
        
        # The running integer that's checked for primeness
        q = 2
        
        while q <= n:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                # 
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next 
                # multiples of its witnesses to prepare for larger
                # numbers
                # 
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            
            q += 1



if __name__ == '__main__':
    sol = Solution()
    n = 100
    for i in sol.prime_generator(n):
        print i,

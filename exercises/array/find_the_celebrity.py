# -*- coding: utf-8 -*-

"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    # O(n^2)
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return -1
        
        i = 0
        while i < n:
            # Find the person who knows nobody if there any.
            j = 0
            while i < n and j < n:
                if j == i or not knows(i, j):
                    j += 1
                else:
                    i += 1
                    j = 0
            
            # If this person doesn't exist, no celebrity is in the party.        
            if i >= n:
                return -1
                
            # If everyone knows this person, he is a celebrity.     
            k = 0
            while k < n:
                if k == i or knows(k, i):
                    k += 1
                    if k >= n:
                        return i
                else: 
                    i += 1
                    break
        return -1
        

        # O(n)
        def findCelebrity(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n < 2:
                return -1
            
            x = 0
            for i in xrange(1, n):
                if knows(x, i):
                    x = i
            # Now 0 ~ x-1 cann't be a celebrity because they are not known by the current x or a preview x.
            # x+1 ~ n-1 cann't be a celebrity neither because the current x doesn't know them.
            
            # Check if the current x is known by everyone in 0 ~ x-1 and he/she doesn't know anyone in 0 ~ x-1.
            for i in xrange(x):
                if not knows(i, x) or knows(x, i):
                    return -1
                    
            # Check if the current is known by everyone in x+1 ~ n-1.
            for i in xrange(x+1, n):
                if not knows(i, x):
                    return -1
                    
            return x
            
# -*- coding: utf-8 -*-

"""
Flavius Josephus was a roman historian of Jewish origin. During the Jewish-Roman wars of the first century AD, he was in a cave with fellow soldiers, 40 men in all, surrounded by enemy Roman troops. They decided to commit suicide by standing in a ring and counting off each third man. Each man so designated was to commit suicide...Josephus, not wanting to die, managed to place himself in the position of the last survivor.

In the general version of the problem, there are n soldiers numbered from 1 to n and each k-th soldier will be eliminated. The count starts from the first soldier. What is the number of the last survivor?
"""

class Person(object):

    def __init__(self, pos):
        self.pos = pos
        self.alive = True

    def __str__(self):
        return 'Person #{}, {}'.format(self.pos, self.alive)

    # Create a linked list with n people. Return the last person.
    def create_linked_list(self, n):
        if n > 0:
            self.next = Person(self.pos + 1)
            return self.next.create_linked_list(n - 1)
        return self

    # Kill every kth living person in a circle
    # Return the final survivor.
    # O(kn)
    def kill(self, pos, k, remaining):
        # Skip this person if he is already dead.
        if not self.alive:
            return self.next.kill(pos, k, remaining)
        # The last living person is the survivor.
        if remaining == 1:
            return self
        # Kill the kth person.
        if pos == k:
            self.alive = False
            pos = 0 # Reset the position counter.
            remaining -= 1  # Decrement the remaining counter.
        return self.next.kill(pos + 1, k, remaining)


# O(n)
# Using 0-based index, people count from 0 to k-1, and the person who counts k-1 will be eliminated.
# Let the survivor in the first round be in position: f(n, k).
# Then the survivor in the second round is in position: f(n-1, k)
# Position in first round --------- Position in second round
# k%n ----------------------------- 0
# (k+1)%n ------------------------- 1
# (k+2)%n ------------------------- 2
# ...
# (k+f(n-1,k))%n ------------------ f(n-1,k)
# f(n, k) = (k+f(n-1,k)) % n
def josephus_dp(n, k):
    result = 0 # In the last round (1 person left), the survivor's position is 0.
    # Loop starting from the second last round (2 people left) to the first round (n people left)
    for i in xrange(2, n+1):
        result = (k + result) % i

    return result + 1   # We need 1-based index.


if __name__ == '__main__':
    n, k = 8, 3
    first = Person(1)
    last = first.create_linked_list(n - 1)
    last.next = first   # Create a circular linked list.
    survivor = first.kill(1, k, n)
    print survivor

    print josephus_dp(n, k)

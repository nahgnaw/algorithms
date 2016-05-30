# -*- coding: utf-8 -*-

"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.d = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.d[number] = self.d.setdefault(number, 0) + 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.d:
            diff = value - i
            if diff in self.d and (self.d[diff] > 1 or diff != i):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

if __name__ == '__main__':
    c = TwoSum()
    c.add(9200)
    c.add(-23)
    c.add(0)
    c.add(1)
    c.add(1)
    print c.find(2)
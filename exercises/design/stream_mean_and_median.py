# -*- coding: utf-8 -*-

"""
Design a class to read integers from stream data and return the current mean and median. Input value range: [0, 1000]
"""


class StreamInt(object):

    def __init__(self):
        self.data = [0] * len(xrange(0, 1000))  # record data frequency
        self.sum = 0
        self.count = 0

    def insert(self, x):
        self.data[x] += 1
        self.sum += x
        self.count += 1

    def get_mean(self):
        if not self.count:
            return None

        return self.sum / float(self.count)

    def get_median(self):
        def find_value_by_index(index):
            count = 0
            for i in xrange(len(self.data)):
                if self.data[i]:
                    count += self.data[i]
                    if index + 1 <= count:
                        return i

        if not self.count:
            return None

        median = [0, 0]
        median_indecies = (self.count / 2, self.count / 2) \
            if self.count % 2 else (self.count / 2 - 1, self.count / 2)
        median[0] = find_value_by_index(median_indecies[0])
        median[1] = find_value_by_index(median_indecies[1])
        return sum(median) / float(2)


if __name__ == '__main__':
    si = StreamInt()
    si.insert(0)
    si.insert(1)
    si.insert(2)
    si.insert(3)
    print si.get_mean()
    print si.get_median()

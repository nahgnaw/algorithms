# -*- coding: utf-8 -*-

"""
There are 4 missing integers in an integer array ranging from 0 to 10^6. Find the missing integers.

Follow-up: what if we only have 32Kb memory?
"""


class Solution(object):
    def missing_integers(self, nums, size=10**6):
        # Assume presence is a bit array.
        # Its size: 1b * 10^6 = 1Mb = 125KB
        presence = [False] * size
        for x in nums:
            nums[x] = True

        missing = []
        for i in xrange(len(presence)):
            if presence[i] == False:
                missing.append(i)

        return missing

    def missing_integers2(self, nums):
        # Divide the 10^6 integers into 10^3 blocks: 0~999, 1000~1999, ...
        # Set up a bucket for each block keeping the count of integers.
        # Size of the count buckets: 32b * 10^3 = 32kb
        # Whichever bucket doesn't have 1000 as the count has missing integers in it.
        # Look at integers in this bucket and find the missing integers.
        counts = [0] * 1000
        for x in nums:
            counts[x/1000] += 1

        missing = []
        for i, count in enumerate(counts):
            if count < 1000:
                num_block = read_num(i)
                missing.extend(self.missing_integers(num_block, 10**3))
        return missing
        
# -*- coding: utf-8 -*-

"""
Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

We will give you a compare function to compare nut with bolt.

Example
Given nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC'].

Your code should find the matching bolts and nuts.

one of the possible return:

nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG'].

we will tell you the match compare function. If we give you another compare function.

the possible return is the following:

nuts = ['ab','bc','dd','gg'], bolts = ['BC','AA','DD','GG'].

So you must use the compare function that we give to do the sorting.

The order of the nuts or bolts does not matter. You just need to find the matching bolt for each nut.
"""


# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        def get_partition(pivot, arr, left, right):
            pivot_ind = left
            i = left + 1
            while i <= right:
                # Put object smaller than pivot in the beginning of the array, before index pivot_ind
                if compare.cmp(pivot, arr[i]) == 1 or compare.cmp(arr[i], pivot) == -1:
                    pivot_ind += 1
                    arr[i], arr[pivot_ind] = arr[pivot_ind], arr[i]
                    i += 1
                # Find the pivot index, set it the first index temporarily
                elif compare.cmp(pivot, arr[i]) == 0 or compare.cmp(arr[i], pivot) == 0:
                    arr[i], arr[left] = arr[left], arr[i]
                # Leave object greater than pivot alone
                else:
                    i += 1
            # Put pivot at the right place, which is at pivot_ind
            arr[left], arr[pivot_ind] = arr[pivot_ind], arr[left]
            return pivot_ind

        def qsort(left, right):
            if left >= right:
                return

            pivot_ind = get_partition(nuts[left], bolts, left, right)
            get_partition(bolts[pivot_ind], nuts, left, right)
            qsort(left, pivot_ind - 1)
            qsort(pivot_ind + 1, right)

        if not nuts or not bolts:
            return
        if not len(nuts) == len(bolts):
            return

        # Use quick sort
        qsort(0, len(nuts) - 1)

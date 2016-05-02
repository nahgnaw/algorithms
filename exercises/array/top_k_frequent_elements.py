# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def quick_select(left, right):
            pivot = left
            l, r = left, right
            while l < r:
                while l < r and counts[r][1] <= counts[pivot][1]:
                    r -= 1
                while l < r and counts[l][1] >= counts[pivot][1]:
                    l += 1
                counts[l], counts[r] = counts[r], counts[l]
            counts[left], counts[l] = counts[l], counts[left]
            
            if l + 1 == k:
                return counts[:l+1]
            elif l + 1 < k:
                return quick_select(l + 1, right)
            else:
                return quick_select(left, l - 1)
        
        if not nums:
            return []
            
        # Get the counts.
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1
            
        counts = counts.items()
        # Use quick select to get the top k counts.
        return [c[0] for c in quick_select(0, len(counts) - 1)]


if __name__ == '__main__':
    sol = Solution()
    nums = [5,2,5,3,5,3,1,1,3]
    k = 2
    print sol.topKFrequent(nums, k)

        
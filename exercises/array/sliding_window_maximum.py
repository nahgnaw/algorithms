# -*- coding: utf-8 -*-

"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        n = len(nums)
        if not n:
            return []

        res = []
        dq = deque()

        for i in xrange(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        for i in xrange(n - k):
            res.append(nums[dq[0]])

            while dq and dq[0] <= i:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i + k]:
                dq.pop()
            dq.append(i + k)

        res.append(nums[dq[0]])
        return res

    def maxSlidingWindow2(self, nums, k):
        if not nums:
            return []

        from collections import deque

        result = []
        q = deque()
        for i in xrange(len(nums)):
            # Keep numbers in the queue in non-increasing order from top to rear
            while q and nums[i] > q[-1]:
                q.pop()

            q.append(nums[i])

            # Keep the length of the queue no larger than the window size
            if i + 1 > k and q[0] == nums[i - k]:
                q.popleft()

            # Record the leftmost (largest) element in the queue
            if i + 1 >= k:
                result.append(q[0])

        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 1, 0, -1]
    k = 3
    sol = Solution()
    print sol.maxSlidingWindow2(nums, k)

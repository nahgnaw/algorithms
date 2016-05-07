# -*- coding: utf-8 -*-

"""
Given a array of size integers which range from 1 to 100, find the missing numbers.
"""


class Solution(object):
    def find_missing_numbers(self, nums, lower, upper):
        if not nums:
            return []

        results = []
        nums.sort()
        if not nums[0] == lower:
            nums = [lower] + nums
            results.append(lower)
        if not nums[-1] == upper:
            nums += [upper + 1]

        i = 0
        while i < len(nums) - 1:
            if nums[i+1] - nums[i] <= 1:
                i += 1
                continue
            x = nums[i] + 1
            while x < nums[i+1]:
                results.append(x)
                x += 1
            i += 1
        return results


if __name__ == '__main__':
    sol = Solution()
    nums = [2,2,5,6,8,10,13]
    lower, upper = 1, 100
    print sol.find_missing_numbers(nums, lower, upper)

"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms
    
    def permute2(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        permutations = []
        partial_perms = self.permute2(nums[1:])
        for i in xrange(len(nums)):
            for perm in partial_perms:
                p = perm[:]
                p.insert(i, nums[0])
                permutations.append(p)
        return permutations

    def permute3(self, nums):

        def recursively_permute(cur):
            if cur == len(nums) - 1:
                res.append(nums[:])
                return
            for i in xrange(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                recursively_permute(cur + 1)
                nums[cur], nums[i] = nums[i], nums[cur]

        res = []
        recursively_permute(0)
        return res

    # DFS. Remember which position has been visited.
    def permute4(self, nums):
        def dfs(tmp):
            if len(tmp) == len(nums):
                result.append(tmp)
                return
            
            for i in xrange(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(tmp + [nums[i]])
                    visited[i] = False
        
        result = []
        visited = [False] * len(nums)
        dfs([])
        return result
        


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print sol.permute4(nums)

# -*- coding: utf-8 -*-

"""
Given a list of integer sets, merge them until no more two sets can be merged.
    
e.g.:
input:
    [
        {1, 3, 5},
        {2, 4, 6},
        {5, 6},
        {7, 8}
    ]
    
output: 
    [
        {1, 3, 5, 6, 2, 4}
        {7, 8}
    ]
"""


class Solution(object):

    def merge_sets(self, sets):

        def has_overlapping(i, j):
            for x in sets[i]:
                if x in sets[j]:
                    return True
            return False

        def merge(i, j):
            for x in sets[j]:
                sets[i].add(x)
            del sets[j]

        i = 0
        merge_flag = False
        while i < len(sets):
            j = i + 1
            while (j < len(sets)):
                if has_overlapping(i, j):
                    merge(i, j)
                    merge_flag = True
                else:
                    j += 1
            if not merge_flag:
                i += 1
            merge_flag = False
        return sets
    

    # DFS. 
    def merge_sets2(self, sets):
        # Find all the sets sharing elements with s, return the union.
        def dfs(i, s):
            res = s.copy()
            visited[i] = True
            for j in xrange(len(sets)):
                if not visited[j] and not res.isdisjoint(sets[j]):
                    res.update(dfs(j, sets[j]))
            return res

        visited = [False] * len(sets)
        results = []
        for i in xrange(len(sets)):
            if not visited[i]:
                results.append(dfs(i, sets[i]))
        return results


if __name__ == '__main__':
    sol = Solution()
    sets = [set([1,3,5]), set([2,4,6]), set([5,6]), set([7,8])]
    print sol.merge_sets2(sets)

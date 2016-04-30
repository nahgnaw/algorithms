# -*- coding: utf-8 -*-

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(string, tmp):
            if is_valid(string) and len(tmp) == 3:
                result.append('.'.join(tmp + [string]))
                return
            
            for i in xrange(1, min(4, len(string))):
                seg = string[:i]
                if is_valid(seg):
                    dfs(string[i:], tmp + [seg])
                            
        def is_valid(string):
            if not string:
                return False
            if string[0] == '0':
                return string == '0'
            return 0 < int(string) < 256
        
        if len(s) < 4 or len(s) > 12:
            return []
        
        result = []
        dfs(s, [])
        return result
        
        

if __name__ == '__main__':
    s = '25525511135'
    sol = Solution()
    print sol.restoreIpAddresses(s)

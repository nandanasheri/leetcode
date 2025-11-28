'''
brute force - o(n^2) check every possible substring
use a num to keep track and check for every substring if it contains t then res = min(res, len(substr))
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_map = {}
        s_map = {}

        # initialize frequency map
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1
        
        l, r = 0, 0
        res = float("inf")
        res_l, res_r = 0,0

        matches = 0
        l = 0
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                matches += 1

            while matches == len(t_map):
                if r-l+1 < res:
                    res = r-l+1
                    res_l, res_r = l,r
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    matches -= 1
                l += 1

        if res == float("inf"):
            return ""
              
        return s[res_l:res_r+1]

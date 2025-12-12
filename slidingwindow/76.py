class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map = {}
        t_map = {}
        matches = 0
        result = float("inf")
        res_str = ""
        for i in t:
            t_map[i] = t_map.get(i,0) + 1
        
        l = 0
        for r in range(len(s)):
            # print(l,r, s_map)
            char = s[r]
            # if in t -> add to map and check for a match
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1 
                if s_map[char] == t_map[char]:
                    matches += 1
            # print(matches)
            # shift window until it's invalid again if valid window
            while matches == len(t_map):
                if result > r-l+1:
                    result = r-l+1
                    res_str = s[l:r+1]
                char = s[l]
                if char in s_map:
                    s_map[char] -= 1
                    if s_map[char] < t_map[char]:
                        matches -= 1
                l += 1
            
            # shift so boundary is always a match for minimum
            while l < len(s) and s[l] not in t_map:
                l += 1
        
        return res_str
            


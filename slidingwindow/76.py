class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        min_window = [-1, -1]
        min_len = float("infinity")
        t_count = {}
        s_count = {}

        for i in t:
            t_count[i] = 1 + t_count.get(i, 0)
            
        have = 0
        need = len(t_count)

        l = 0
        for r in range(len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
            print(have)
            while have == need:
            
                if min_len > (r-l + 1):
                    min_window = [l,r]
                    min_len = r - l + 1
               
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = min_window
        print(min_window)
        return s[l:r+1] if min_len != float("infinity") else ""
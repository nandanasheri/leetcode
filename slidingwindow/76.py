class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqMap = {}
        s_freqMap = {}
        
        for i in t:
            t_freqMap[i] = t_freqMap.get(i,0) + 1
        
        minlen = float("inf")
        result = ""
        l = 0
        r = 0

        # o(1) because maps are fixed size
        def is_match():
            for i in t_freqMap:
                if i not in s_freqMap:
                    return False
                if s_freqMap[i] < t_freqMap[i]:
                    return False
            return True

        # slide through your window
        while l < len(s) and r < len(s):
            # we always want our window to start at an important char for minimum
            if s[l] not in t_freqMap:
                l += 1
                continue
            # add to freqMap if important
            if s[r] in t_freqMap:
                s_freqMap[s[r]] = s_freqMap.get(s[r], 0) + 1
            
            # check for a match and keep updating result if you find a match
            while is_match():
                if r-l+1 < minlen:
                    minlen = r-l+1
                    result = s[l:r+1]
                if s[l] in s_freqMap:
                    s_freqMap[s[l]] -= 1
                l += 1
            r += 1

        return result

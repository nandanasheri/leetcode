class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()

        res = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 1
        chars.add(s[l])

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            chars.add(s[r])
            r += 1
        
        return res
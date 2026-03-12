class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        chars = set()
        l = 0
        chars.add(s[l])
        result = 1

        for r in range(1, len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            result = max(result, r-l+1)
            chars.add(s[r])

        
        return result
            
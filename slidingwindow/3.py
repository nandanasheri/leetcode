# figured out the algo was only missing a reset condition!!
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        if len(s) == 0:
            return 0
        start, end = 0,0

        chars = set()

        while end < len(s):
            if s[end] not in chars:
                chars.add(s[end])
                max_length = max(max_length, end-start + 1)
                end += 1
            else:
                while s[end] in chars:
                    chars.remove(s[start])
                    start += 1
    
        return max_length

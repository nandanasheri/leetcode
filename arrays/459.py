class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            substr = s[0:i+1]
            if len(s) % len(substr) != 0:
                continue
            num = len(s) // len(substr)
            if num == 1:
                continue
            if substr * num == s:
                return True
        return False
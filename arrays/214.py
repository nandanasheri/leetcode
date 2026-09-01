class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        base = 29
        prefix = 0
        suffix = 0
        last_index = 0
        power = 1

        for i in range(len(s)):
            char = ord(s[i]) - ord('a') + 1
            prefix = prefix * base
            prefix = prefix + char

            suffix = suffix + char * power
            power *= base

            if prefix == suffix:
                last_index = i
        
        suffix = s[last_index+1:]
        return suffix[::-1] + s
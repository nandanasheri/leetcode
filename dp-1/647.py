class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        dp_cache = [[False] * n for _ in range(n)]

        for i in range(n):
            dp_cache[i][i] = True
            result += 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp_cache[i][i+1] = True
                result += 1

        # for lengths greater than or equal to 3
        for k in range(3, n+1):
            
            for i in range(0, n-k+1):
                j = i + k - 1

                if s[i] == s[j] and dp_cache[i+1][j-1]:
                    dp_cache[i][j] = True
                    result += 1
        
        return result
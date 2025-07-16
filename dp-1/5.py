class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]

        maxlen = 1
        res_ind = 0
        
        # strings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # strings of length 2 check if they are palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if maxlen < 2:
                    maxlen = 2
                    res_ind = i
        
        # strings of length greater than 3
        # this loop looks for lengths 3, 4, 5 etc etc
        for k in range(3, n+1):
            for i in range(0, n-k+1):
                j = i + (k-1)
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if (j-i + 1) > maxlen:
                        maxlen = j - i + 1
                        res_ind = i
        
        return s[res_ind:res_ind+maxlen]

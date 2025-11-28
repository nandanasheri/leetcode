class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp_cache = defaultdict(dict)
        res = s[0]

        # smallest subproblems chars of len 1 are all valid palindromes
        for i in range(len(s)):
            dp_cache[i][i] = True

        # len 2 are valid if chars are the same
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp_cache[i][i+1] = True
                res = s[i:i+2]
            else:
                dp_cache[i][i+1] = False
        
        # iterate for len 3 and above by looking at subproblems!
        for i in range(2, len(s)):
            for j in range(0, len(s)-i):
                l,r = j, i+j
                if s[l] == s[r] and dp_cache[l+1][r-1] == True:
                    dp_cache[l][r] = True
                    if r-l+1 > len(res):
                        res = s[l:r+1]
                else:
                    dp_cache[l][r] = False
        
        return res

class Solution:
    def numDecodings(self, s: str) -> int:
        dp_cache = {len(s) : 1}

        def dfs(i):
            if i in dp_cache:
                return dp_cache[i]
            if s[i] == "0":
                return 0
            
            # take only first digit
            res = dfs(i+1)

            if (i < len(s) - 1) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                res += dfs(i+2)
            
            dp_cache[i] = res
            return res
        
        return dfs(0)
        
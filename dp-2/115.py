class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        result = 0
        # edge cases 
        if m < n:
            return 0
        if m == n:
            return int(s == t)
        cache = {}

        def dfs(i,j):
            if j == n:
                return 1
            if i == m:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                cache[(i,j)] =  dfs(i+1, j)
            return cache[(i,j)]
        
        return dfs(0,0)

            


        
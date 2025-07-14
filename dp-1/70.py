class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp_cache = [-1] * (n+1)
        dp_cache[n], dp_cache[n-1] = 1, 1

        for i in range(n-2, -1, -1):
            dp_cache[i] = dp_cache[i+1] + dp_cache[i+2]
        
        
        return dp_cache[0]

        
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        # brute force solution
        def _climb(currsteps):
            nonlocal res
            if currsteps == n:
                res += 1
                return
            if currsteps > n:
                return
            _climb(currsteps+1)
            _climb(currsteps+2)
        
        # add a DP Cache to it - top down DP
        dp_cache = {}
        def _climbcache(currsteps):
            nonlocal res
            if currsteps in dp_cache:
                return dp_cache[currsteps]
            if currsteps == n:
                return 1
            if currsteps > n:
                return 0
            dp_cache[currsteps] = _climbcache(currsteps+1) + _climbcache(currsteps+2)
            return dp_cache[currsteps]
        # _climbcache(0)

        # bottom up DP
        dp_cache = [0] * (n+1)
        for i in range(n, -1, -1):
            if i == n-1 or i == n:
                dp_cache[i] = 1
                continue
            dp_cache[i] = dp_cache[i+1] + dp_cache[i+2]
        # print(dp_cache)
        return dp_cache[0]

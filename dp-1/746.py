class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # top down DP
        dp_cache = {}
        def _minCost(i, currcost):
            if i in dp_cache and currcost < dp_cache[i]:
                dp_cache[i] = currcost
            if i >= len(cost):
                return currcost
            dp_cache[i] = min(_minCost(i+1, currcost+cost[i]), _minCost(i+2, currcost+cost[i]))
            return dp_cache[i]
        # return min(_minCost(0, 0), _minCost(1,0))
        
        dp_cache = [0] * len(cost)
        n = len(cost)
        for i in range(n-1, -1, -1):
            if i == n-1 or i == n-2:
                dp_cache[i] = cost[i]
                continue
            dp_cache[i] = cost[i] + min(dp_cache[i+1], dp_cache[i+2])
        return min(dp_cache[0], dp_cache[1])
            

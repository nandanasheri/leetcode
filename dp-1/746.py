class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_cache = [0] * len(cost)

        dp_cache[-1] = cost[-1]
        dp_cache[-2] = cost[-2]

        if len(cost) == 2:
            return min(dp_cache[0], dp_cache[1])

        for i in range(len(dp_cache)-3, -1, -1):
            dp_cache[i] = cost[i] + min(dp_cache[i+1], dp_cache[i+2])
        
        return min(dp_cache[0], dp_cache[1])
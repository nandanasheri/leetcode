class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp_cache = {}
        def dfs(total, i):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
                    
            if (total,i) in dp_cache:
                return dp_cache[(total,i)]

            dp_cache[(total,i)] = dfs(total+nums[i], i+1) + dfs(total-nums[i], i+1)
            return dp_cache[(total,i)]
            
        return dfs(0,0)

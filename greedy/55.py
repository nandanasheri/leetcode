class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        # greedily shift the goal post closer and closer to us if it's reachable from the current position
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0
    
    # top down DP solution that made sense
    class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        dp[len(nums) - 1] = True

        def dfs(i):

            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            
            end = i + nums[i] + 1

            for j in range(i+1, end):
                if dfs(j):
                    dp[j] = True
                    return True

            dp[i] = False
            return False
        
        return dfs(0)
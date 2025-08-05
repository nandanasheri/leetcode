class Solution:
    def jump(self, nums: List[int]) -> int:
        # bottom up DP solution
        dp = [len(nums)] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2, -1, -1):

            if nums[i] == 0:
                dp[i] = len(nums)
                continue
            
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    dp[i] = min(dp[i+j]+1, dp[i])
                

        return dp[0]
        
        # Greedy Solution
        l,r = 0,0
        res = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, nums[i]+i)
            l = r+1
            r = farthest
            res += 1
        return res
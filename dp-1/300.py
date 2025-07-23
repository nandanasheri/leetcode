class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_cache = [1] * len(nums)
        dp_cache[-1] = 1
    

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp_cache[i] = max(dp_cache[i], 1+dp_cache[j])
        
        return max(dp_cache)
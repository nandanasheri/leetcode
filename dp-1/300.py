class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp_cache = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            # print(dp_cache)
            if i == len(nums) - 1:
                continue
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp_cache[i] = max(dp_cache[i], dp_cache[j]+1)

        return max(dp_cache)

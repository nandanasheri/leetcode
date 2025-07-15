class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_cache = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp_cache[-1] = nums[-1]
        dp_cache[-2] = nums[-2]
        curr_max = nums[-1]

        for i in range(len(nums)-3, -1, -1):
            dp_cache[i] = nums[i] + curr_max
            curr_max = max(curr_max, dp_cache[i+1])
    
        return max(dp_cache[0], dp_cache[1])


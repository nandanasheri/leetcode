class Solution:
    def rob(self, nums: list[int]) -> int:
   
        if len(nums) <= 3:
            return max(nums)
        
        def _bottomUpRob(subarr):
            dp_cache = [0] * len(subarr)
            n = len(subarr)
            # bottom up DP for first subarray
            for i in range(n-1, -1, -1):
                if i == n-1:
                    dp_cache[i] = subarr[n-1]
                    continue
                if i == n-2:
                    dp_cache[i] = max(subarr[i], dp_cache[i+1])
                    continue
                dp_cache[i] = max(subarr[i] + dp_cache[i+2], dp_cache[i+1])
            return dp_cache[0]
        
        return max(_bottomUpRob(nums[:-1]), _bottomUpRob(nums[1:]))
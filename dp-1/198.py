class Solution:
    def rob(self, nums: list[int]) -> int:
        result = 0

        def _rob(i, amt):
            nonlocal result
            if i == len(nums)-1 or i == len(nums)-2:
                result = max(result, amt)
                return
            for j in range(i+2, len(nums)):
                _rob(j, amt+nums[j])
        
        # for i in range(len(nums)):
        #     _rob(i,nums[i])
        # return result            

        dp_cache = [0] * len(nums)
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp_cache[i] = nums[i]
                continue
            if i == n-2:
                dp_cache[i] = max(nums[i], dp_cache[i+1])
                continue
            # either we choose to include current house, or skip it for something better in the future.
            dp_cache[i] = max(nums[i] + dp_cache[i+2], dp_cache[i+1])
        
        return max(dp_cache[0], dp_cache[1])


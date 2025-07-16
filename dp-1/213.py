class Solution:
    def rob(self, nums: List[int]) -> int:

        def house_robber_i(nums):
           
            dp_cache = [0] * len(nums)
            if len(nums) == 1:
                return nums[0]
            # adjacent - cannot rob either
            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            dp_cache[-1] = nums[-1]
            dp_cache[-2] = nums[-2]

            curr_max = dp_cache[-1]
            
            for i in range(len(nums) - 3, -1, -1):
                dp_cache[i] = nums[i] + curr_max
                curr_max = max(curr_max, dp_cache[i+1])

           
            return max(dp_cache[0], dp_cache[1])

        if len(nums) == 1:
                return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # run house robber I twice on two different sub arrays excluding first and last house!
        max_a = house_robber_i(nums[1:])
        max_b = house_robber_i(nums[0:-1])

        return max(max_a, max_b)
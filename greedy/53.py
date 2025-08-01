class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = float("-infinity")
    
        for i in range(len(nums)):
            if prefix < 0:
                prefix = nums[i]
            else:
                prefix += nums[i]
            res = max(res, prefix)
        return res
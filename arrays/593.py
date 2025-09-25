class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums)-2):
            # check for triangle inequality
            if nums[i] + nums[i+1] > nums[i+2] and nums[i+1] + nums[i+2] > nums[i] and nums[i] + nums[i+2] > nums[i+1]:
                result = max(result, nums[i] + nums[i+1] + nums[i+2])
        
        return result
'''
nums = [1,-2,3,-2]
find subarray with maximum sum - circular array

[5,-3,-2,5]
brute force ; every possible subarray

total_sum - sum(minimum_subarr)
total =  5


'''
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        currMin, currMax = 0,0
        globalMin, globalMax = nums[0], nums[0]
        total = sum(nums)
        isNegative = True

        # Kadane's Algorithm
        for num in nums:
            # print(currMin, currMax, globalMin, globalMax)
            if num >= 0:
                isNegative = False
            if num+currMin < num:
                currMin += num
            else:
                currMin = num
            if num+currMax > num:
                currMax += num
            else:
                currMax = num
            globalMin = min(globalMin, currMin)
            globalMax = max(globalMax, currMax)
        
        if isNegative:
            return max(nums)
        return max(globalMax, total-globalMin)

        
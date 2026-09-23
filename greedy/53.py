'''
result = 6
currsum = 5
i = 2
nums = [-2,1,-3,4,-1,2,1,-5,4]
                l
              r
nums = [5,4,-1,7,8]
        l
             r
o(n^2)
for i in nums:
    for j in nums:
        [go through every possible subarray]
        if [i:j] > currsum:
            currsum = new sum

result = nums[0]
currsum = [0]
for i (1, len(nums)):
    check if the currsum + nums[i] < nums[i]:
        reset currsum = nums[i]
    else:
        currsum += nums[i]
    result = max(result, currsum)
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        currsum = nums[0]

        for i in range(1, len(nums)):
            if currsum + nums[i] < nums[i]:
                currsum = nums[i]
            else:
                currsum += nums[i]
            result = max(result, currsum)
            
        return result
        
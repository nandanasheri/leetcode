'''
[2,3,1,2,4,3]
         l
           r
target = 7
currsum = 7
res = float("inf")
if at a valid window as you shift l, update result
check for valid window if currsum >= target
sum(nums) < target: return 0
condition to increment l:
    while currsum >= target:
        update res
        currsum -= nums[l]
        l += 1
res = 3

'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        result = float("inf")
        l = 0

        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                result = min(result, r-l+1)
                currsum -= nums[l]
                l += 1
        if result == float("inf"):
            return 0
        return result
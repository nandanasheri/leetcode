class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = 0
        if len(nums) == 1:
            return nums[0]
        
        currsum = 0
        l = 0
        for r in range(len(nums)):
            currsum += nums[r]
            if r-l+1 == k:
                if result != 0:
                    result = max(result, currsum/k)
                else:
                    result = currsum/k
                currsum -= nums[l]
                l += 1
        
        return result
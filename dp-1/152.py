class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax, currmin = 1,1
        result = max(nums)

        for i in nums:
            if i == 0:
                currmax, currmin = 1,1
                continue
            temp = currmax
            currmax = max(currmax * i, currmin*i, i)
            currmin = min(temp * i, currmin*i, i)
            result = max(result, currmax)
        
        return result
        
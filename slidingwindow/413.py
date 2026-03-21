class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        l = 0
        r = 1

        if len(nums) <= 2:
            return 0

        currdiff = nums[1] - nums[0]
        
        while r < len(nums):
            if (nums[r]-nums[r-1]) != currdiff:
                l = r-1
                currdiff = nums[r] - nums[r-1]
            windowLen = r-l+1
            if windowLen >= 3:
                # print(windowLen, l, r)
                result += (windowLen-3) + 1
            r += 1

        return result
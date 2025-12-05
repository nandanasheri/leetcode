class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            elif nums[i] == 0:
                ones = 0
            result = max(result,ones)

        return result
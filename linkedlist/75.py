'''
n objects - guaranteed only 3 colors -
sort and modify in place 
nums = [2,0,2,1,1,0]

o(n) time - o(1) constant space
''' 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes, ones, twos = 0,0,0
        for i in nums:
            if i == 0:
                zeroes += 1
            elif i == 1:
                ones += 1
            elif i == 2:
                twos += 1
        
        for i in range(len(nums)):
            if zeroes > 0:
                nums[i] = 0
                zeroes -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            elif twos > 0:
                nums[i] = 2
                twos -= 1
        
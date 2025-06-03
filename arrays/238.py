# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix_arr = [1] * (len(nums) + 1)  
        postfix_arr = [1] * (len(nums) + 1) 
        for i in range(len(nums)):
            prefix_arr[i+1] = prefix_arr[i] * nums[i]

        for i in range(len(nums)-1, -1, -1):
            postfix_arr[i] = postfix_arr[i+1] * nums[i]

        for i in range(1, len(prefix_arr)):
            answer[i-1] = prefix_arr[i-1] * postfix_arr[i]
        return answer
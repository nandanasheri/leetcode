class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curr_min = nums[0]
        for i in range(1,len(nums)):
            # print(stack)
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            # stack is empty add to it
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True
                
            stack.append((nums[i], curr_min))
            curr_min = min(curr_min, nums[i])
        return False
            


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = []
        pick = [False] * len(nums)

        def backtrack(i):
            if len(curr) == len(nums):
                result.append(curr.copy())
            for j in range(len(nums)):
                if not pick[j]:
                    pick[j] = True
                    curr.append(nums[j])
                    backtrack(j)
                    curr.pop()
                    pick[j] = False
        
        backtrack(0)
        return result
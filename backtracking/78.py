class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = []

        def dfs(i):
            if i == len(nums):
                result.append(curr.copy())
                return
            # add nums[i] to curr and recurse
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            # recurse without adding nums[i]
            dfs(i+1)
        
        dfs(0)
        return result

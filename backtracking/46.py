class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = []
        currset = set()
        
        def dfs(i):
            # print(i,curr)
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            if i >= len(nums):
                return

            for j in range(len(nums)):
                if nums[j] not in currset:
                    curr.append(nums[j])
                    currset.add(nums[j])
                    dfs(j)
                    curr.pop()
                    currset.remove(nums[j])

        dfs(0)
        return result
            
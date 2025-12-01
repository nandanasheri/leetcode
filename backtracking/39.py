class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        currsum = 0
        curr = []

        def dfs(i,currsum):
            # print(curr)
            if currsum == target:
                result.append(curr.copy())
                return
            if currsum > target:
                return
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dfs(j, currsum+candidates[j])
                curr.pop()
        dfs(0,0)
        return result
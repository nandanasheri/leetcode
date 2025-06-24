class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        result = []

        def dfs(i, currsum):

            if currsum == target:
                result.append(curr.copy())
                return
            if currsum > target:
                return
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dfs(j,  currsum +candidates[j])
                x = curr.pop()
        
        dfs(0, 0)
        return result

            
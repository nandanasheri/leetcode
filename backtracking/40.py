class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr = []

        def dfs(i, currsum):

            if currsum == target:
                result.append(curr.copy())
                return
            if i == len(candidates) or currsum > target:
                return

            # include candidates[i]
            curr.append(candidates[i])
            dfs(i+1, currsum + candidates[i])
            curr.pop()

            # skip candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currsum)

        dfs(0,0)
        return result
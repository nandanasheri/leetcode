class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        currsum = 0
        result = []
        candidates.sort()
    
        def dfs(i,currsum):
            # print(i, curr)
            if currsum == target:
                result.append(curr.copy())
                return
            if currsum > target or i >= len(candidates):
                return
            # we either choose to include the current number
            curr.append(candidates[i])
            # and we move on to the next - which could possible use the same value
            dfs(i+1,currsum+candidates[i])
            curr.pop()
            # or we choose to skip it
            # we can't do what we do in CS1 because we just don't start a NEW call with same number
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, currsum)

            
        
        dfs(0,0)
        return result
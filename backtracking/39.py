class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def _combinationSum(i, currsum):
            if currsum > target or i == len(candidates):
                return
            if currsum == target:
                result.append(curr[::])
                return
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                _combinationSum(j, currsum+candidates[j])
                curr.pop()
        
        _combinationSum(0,0)
        return result

            
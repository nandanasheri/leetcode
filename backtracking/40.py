class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        candidates.sort()

        def _combinationSum(i,currsum):
            # print(curr)
            if currsum == target:
                result.append(curr[::])
                return
            if i == len(candidates) or currsum > target:
                return
            
            curr.append(candidates[i])
            _combinationSum(i+1, currsum+candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            _combinationSum(i+1, currsum)
                    
        
        _combinationSum(0,0)
        return result
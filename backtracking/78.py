class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        currlist = []
        def _subsets(i):
            # we have two choices - either we add it or we don't
            if i >= size:
                result.append(currlist.copy())
                return
            
            currlist.append(nums[i])
            _subsets(i+1)
            currlist.pop()
            _subsets(i+1)
        
        _subsets(0)
        return result
            
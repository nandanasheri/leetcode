class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = []
        nums.sort()

        def _backtrack(i):
            if i >= len(nums):
                result.append(curr.copy())
                return
            # choosing to include nums[i]
            curr.append(nums[i])
            _backtrack(i+1)
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            _backtrack(i+1)

        _backtrack(0)
        return result
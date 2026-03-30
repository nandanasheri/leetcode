class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        currset = set()

        def permute():
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            
            for i in nums:
                if i not in currset:
                    curr.append(i)
                    currset.add(i)
                    permute()
                    curr.pop()
                    currset.remove(i)
        permute()
        return result
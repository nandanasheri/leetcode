class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = []
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i,0)

        def dfs():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return

            for j in counts:
                if counts[j] > 0:
                    curr.append(j)
                    counts[j] -= 1
                    dfs()
                    curr.pop()
                    counts[j] += 1

        dfs()
        return result
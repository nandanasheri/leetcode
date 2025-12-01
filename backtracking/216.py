class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        currsum = 0
        curr = []

        def dfs(i,currsum):
            # print(i,curr)
            if len(curr) == k and currsum == n:
                result.append(curr.copy())
                return
            if currsum > n or len(curr) > k or i > 9:
                return
            curr.append(i)
            dfs(i+1, currsum+i)
            curr.pop()
            dfs(i+1, currsum)
        dfs(1,0)
        return result
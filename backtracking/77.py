class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []

        def dfs(i):
            # print(i, curr)
            if len(curr) == k:
                result.append(curr.copy())
                return

            for j in range(i+1,n+1):
                curr.append(j)
                dfs(j)
                curr.pop()
        dfs(0)
        return result
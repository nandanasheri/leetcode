# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            # out of bounds
            if i < 0 or i >= m or j < 0 or j >=n :
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"

                # traverse through
                dfs(i+1, j) 
                dfs(i-1, j) 
                dfs(i, j+1) 
                dfs(i, j-1) 

        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num += 1
        return num

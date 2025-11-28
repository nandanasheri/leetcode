class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            nonlocal area
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            area += 1
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(i+x, j+y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area, area)
        return max_area
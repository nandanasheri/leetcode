class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        result = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i >= m or i < 0 or j >= n or j < 0 or (i,j) in visited or grid[i][j] == "0":
                return 
            visited.add((i,j))
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(i+x, j+y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    result += 1
        
        return result

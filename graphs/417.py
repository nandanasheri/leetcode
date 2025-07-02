class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        m = len(heights)
        n = len(heights[0])

        def dfs(i,j, visited):
            visited.add((i,j))

            for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                if i+x < 0 or i+x >= m or j+y < 0 or j+y >= n or (i+x,j+y) in visited:
                    continue

                if heights[i+x][j+y] >= heights[i][j]:
                    dfs(i+x, j+y, visited)

        # only border cells - pacific
        for i in range(n):
            dfs(0, i, pacific)
        for i in range(m):
            dfs(i, 0, pacific)

        # atlantic border cells
        for i in range(n):
            dfs(m-1, i, atlantic)
        for i in range(m):
            dfs(i, n-1, atlantic)

        intersection = pacific & atlantic
        result = []
        for i in intersection:
            result.append(list(i))
        
        return result



class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp_cache = {}
        visited = set()
        m = len(matrix)
        n = len(matrix[0])

        def dfs(i,j):
            if (i,j) in dp_cache:
                return dp_cache[(i,j)]
            visited.add((i,j))
            curr_max = 1
            for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
                a = i+x
                b = j+y
                if 0<=a<m and 0<=b<n and (a,b) not in visited and matrix[i][j] < matrix[a][b]:
                    curr_max = max(curr_max, 1+dfs(a,b))
            dp_cache[(i,j)] = curr_max
            visited.remove((i,j))
            return curr_max
        
        for i in range(m):
            for j in range(n):
                visited.clear()
                dfs(i,j)
        
        return max(list(dp_cache.values()))
        

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp_cache = []

        for i in range(m):
            each = []
            for j in range(n):
                each.append(-1)
            dp_cache.append(each)
    

        def dfs(i,j):
            if dp_cache[i][j] != -1:
                return dp_cache[i][j]
            
            for each in [(1,0), (0,1), (-1,0), (0,-1)]:
                x, y = i + each[0], j + each[1]
                # out of bounds
                if (0 <= x < m) and (0 <= y < n) and matrix[x][y] > matrix[i][j]:
                    dp_cache[i][j] = max(dp_cache[i][j], 1 + dfs(x,y))
                else:
                    dp_cache[i][j] = max(dp_cache[i][j], 1)
            
            return dp_cache[i][j]
        
        for i in range(m):
            for j in range(n):
                dfs(i,j)
      
        result = -1
        for i in range(m):
            for j in range(n):
                result = max(result, dp_cache[i][j])
        return result

        
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_path = float("inf")
        visited = set()
        q = deque()
        if grid[0][0] == 0:
            q.append((0,0,1))
        
        while q:
            i,j,path = q.popleft()
            if (i,j) in visited:
                continue
            if i == m-1 and j == n-1:
                min_path = min(min_path, path)
                continue
            visited.add((i,j))
            for x,y in [(1,0), (0,1), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y] == 0 and (i+x,j+y) not in visited:
                    q.append((i+x, j+y, path+1))
        
        if min_path == float("inf"):
            return -1
        return min_path

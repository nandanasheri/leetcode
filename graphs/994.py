class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        minutes = 0
        neighbors = [(1, 0), (-1,0), (0,1), (0,-1)]
        # add all rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q:
            # print(q)
            for i in range(len(q)):
                cell = q.popleft()

                for each in neighbors:
                    x = cell[0] + each[0]
                    y = cell[1] + each[1]

                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
            minutes += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        if minutes > 0: return minutes-1
        else: return 0


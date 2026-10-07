'''
[[2,2,1],
 [2,1,0],
 [0,1,2]
 [0,2,2]]

 do a BFS on every rotten orange
 every iter of BFS is a minute
 queue [[0,0][3,2]]
 while q is not empty:
    # level by level
    for every in q:
        pop off the queue
        mark neighbors as rotten if orange
        add neighbord to q
    minutes += 1
return minutes

'''
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minutes = 0
        queue = deque()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while queue:
            for i in range(len(queue)):
                x,y = queue.popleft()
                for a,b in [(1,0), (0,1), (-1,0), (0,-1)]:
                    if a+x < 0 or a+x >= m or b+y < 0 or b+y >= n or grid[a+x][b+y] != 1:
                        continue
                    grid[a+x][b+y] = 2
                    queue.append((a+x, b+y))
            minutes += 1
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        if minutes == 0:
            return 0
        
        return minutes - 1
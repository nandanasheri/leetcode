class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = []
        m = len(mat)
        n = len(mat[0])
        # setting up the 2D result grid with zeroes and large values otherwise
        for i in range(m):
            each = []
            for j in range(n):
                if mat[i][j] == 0:
                    each.append(0)
                else:
                    each.append(m*n)
            result.append(each)
        
        # perform a BFS on every zero found
        
        # print(f"Inside BFS {i,j}")
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    
        visited = set()
        while q:
            x,y,dist = q.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
                x_i = x+a
                y_j = y+b
                if 0 <= x_i < m and 0 <= y_j < n and mat[x_i][y_j] != 0 and (x_i, y_j) not in visited:
                    if result[x_i][y_j] > dist+1:
                        result[x_i][y_j] =  dist+1
                        # only want to do a BFS if these values are decreasing
                        q.append((x_i, y_j, dist+1))

        return result
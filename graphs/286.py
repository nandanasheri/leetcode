class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        q = deque()
        visited = set()
        m = len(rooms)
        n = len(rooms[0])
        # add all gates to matrix
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        while q:
            print(q)
            for k in range(len(q)):
                i,j = q.popleft()
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                for x,y in [(0,1), (1,0), (-1,0), (0,-1)]:
                    new_i, new_j = i+x, j+y
                    if 0<=new_i<m and 0<=new_j<n and (new_i,new_j) not in visited and rooms[new_i][new_j] != -1:
                        rooms[new_i][new_j] = min(rooms[new_i][new_j], 1+rooms[i][j])
                        q.append((new_i,new_j))
        

        

        
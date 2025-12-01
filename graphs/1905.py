class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        parent = []
        rank = []
        # build parent matrix and rank matrix
        for i in range(m):
            each = []
            each_rank = []
            for j in range(n):
                if grid2[i][j] == 1:
                    each.append((i,j))
                    each_rank.append(1)
                else:
                    each.append(-1)
                    each_rank.append(0)
            parent.append(each)
            rank.append(each_rank)
        
        def find(node):
            i,j = node
            while (i,j) != parent[i][j]:
                # path compression
                parent[i][j] = parent[parent[i][j][0]][parent[i][j][1]]
                i,j = parent[i][j]
            return (i,j)
        
        def union(e1,e2):
            i1,j1 = find(e1)
            i2,j2 = find(e2)
            if (i1,j1) == (i2,j2):
                return
            if rank[i1][j1] > rank[i2][j2]:
                parent[i2][j2] = (i1,j1)
                rank[i1][j1] += 1
            else:
                parent[i1][j1] = (i2,j2)
                rank[i2][j2] += 1

        # connect edges within the islands
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    # found an island - connect them four directionally
                    visited.add((i,j))
                    for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                        if 0<=i+x<m and 0<=j+y<n and (i+x,j+y) not in visited and grid2[i+x][j+y]== 1:
                            union((i,j),(i+x,j+y))
        
        connected_components = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    connected_components[find((i,j))].append((i,j))
        
        result = 0
        for comp in connected_components:
            edges = connected_components[comp]
            sub_island = True
            for i,j in edges:
                if grid1[i][j] != 1:
                    sub_island = False
            if sub_island:
                result += 1
        
        return result
        



        
        
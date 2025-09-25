def canReach(points: list) -> bool:
    start = (points[0], points[1])
    target = (points[2], points[3])
    dp_cache = {}

    def dfs(i,j):
        if (i,j) in dp_cache:
            return dp_cache[(i,j)]
        if (i,j) == target:
            dp_cache[(i,j)] = True
            return True
        if i > target[0] or j > target[1]:
            dp_cache[(i,j)] = False
            return False
        dp_cache[(i,j)] = dfs(i, i+j) or dfs(i+j, j)
        return dp_cache[(i,j)]
    
    return dfs(start[0], start[1])

points = [1,1,2,2]

print(canReach(points))
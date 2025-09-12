class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target = (m-1, n-1)
        # 2D cache - make sure to initialize your cache like this!!
        cache = [[-1] * n for _ in range(m)]

        def _dfs(i, j):

            print(i,j, cache)
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0

            # check if result is cached
            if cache[i][j] != -1:
                return cache[i][j]

            # go right and go down
            cache[i][j] = _dfs(i, j+1) + _dfs(i+1, j)
            return cache[i][j]

        return _dfs(0,0)
        
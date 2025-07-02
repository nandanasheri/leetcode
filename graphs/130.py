class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        # run dfs solely for border O's to get unsurrounded regions
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        # print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
        return
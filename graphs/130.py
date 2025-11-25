class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def dfs(i,j):
            if i < 0 or i>=m or j < 0 or j>=n or board[i][j] != "O": 
                return
            board[i][j] = "A"
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                dfs(i+x, j+y)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
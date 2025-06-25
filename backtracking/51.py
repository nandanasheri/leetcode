class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for i in range(n)]
        
        cols = set()
        pos_diag = set()
        neg_diag = set()

        def dfs(r):
            if r == n:
                copy = []
                for i in range(n):
                    copy.append("".join(board[i]))
                result.append(copy)
                return

            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                dfs(r+1)
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        dfs(0)
        return result

        
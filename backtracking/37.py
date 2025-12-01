class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    subgrids[(i//3,j//3)].add(int(board[i][j]))
                else:
                    empty.append((i,j))
        
        # print(rows, cols, subgrids)
        
        def dfs(idx):
            # we have solved everything
            if idx == len(empty):
                return True
            # the position that needs to be solved
            i,j = empty[idx]
            # print(i,j)
            for k in range(1,10):
                # already there
                if k in rows[i] or k in cols[j] or k in subgrids[(i//3,j//3)]:
                    continue
                # if valid, place k on the board add to our sets and recurse
                rows[i].add(k)
                cols[j].add(k)
                subgrids[(i//3,j//3)].add(k)
                board[i][j] = str(k)
                # if the future is a valid solution, then don't backtrack
                if dfs(idx+1):
                    return True
                rows[i].remove(k)
                cols[j].remove(k)
                subgrids[(i//3,j//3)].remove(k)
                board[i][j] = "."
            return False
        
        dfs(0)
                

                        
        
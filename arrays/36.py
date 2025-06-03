# [[".",".",".",".","5",".",".","1","."],
#  [".","4",".","3",".",".",".",".","."],
#  [".",".",".",".",".","3",".",".","1"],
#  ["8",".",".",".",".",".",".","2","."],
#  [".",".","2",".","7",".",".",".","."],
#  [".","1","5",".",".",".",".",".","."],
#  [".",".",".",".",".","2",".",".","."],
#  [".","2",".","9",".",".",".",".","."],
#  [".",".","4",".",".",".",".",".","."]]

# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        # Hashset solution 
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set) # key will be the sub grid position like row/3, col/3

        for i in range (9):
            for j in range (9):
                if board[i][j] not in nums:
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grids[(i//3,j//3)]:
                    return False
                rows[i].add(board[i][j]) 
                cols[j].add(board[i][j])
                grids[(i//3, j//3)].add(board[i][j])
        
        # Set solution - using multiple sets brute force technique
        ''' for i in range(9):
            dup_row = set() 
            dup_col = set()

            for j in range(9):
                if board[i][j] in dup_row or board[j][i] in dup_col:
                    return False

                if board[i][j] not in dup_row and board[i][j] in nums:
                    dup_row.add(board[i][j])
                if board[j][i] not in dup_col and board[j][i] in nums:
                    dup_col.add(board[j][i])
        
        for i in range(9):
            dup_subgrid = set()
            for j in range(3):
                for k in range(3):
                    row = (i//3) * 3 + j
                    col = (i%3) * 3 + k
                    item = board[row][col]
                    if item in dup_subgrid:
                        return False
                    if item in nums:
                        dup_subgrid.add(item)'''

        return True
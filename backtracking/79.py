'''
backtracking_func(i, r, c):
    if i == len(word):
        return true
    for x,y in [four directions wrt r and c]:
        if in bounds AND if [x][y] == word[i+1]:
            i += 1
            change character to be empty
            backtrack(i)
            i -= 1

entry point
for m in board:
    for n in board:
        if [m][n] == word[0]:
            change character to be empty
            if backtracking(0):
                return true
return false
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def _backtrack(ind, r, c):
            # print(ind, r, c)
            # iterated through entire word
            if ind == len(word)-1:
                return True
            # all four directions
            for x,y in [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]:
                if 0 <= x < m and 0 <= y < n and word[ind+1] == board[x][y]:
                    board[x][y] = ""
                    if _backtrack(ind+1, x, y):
                        return True
                    board[x][y] = word[ind+1]
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    if _backtrack(0,i,j):
                        return True
                    board[i][j] = word[0]
                    
        return False
        
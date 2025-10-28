'''
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]],

 ind = 0
 iterate through and perform dfs if [i][j] = word[ind]
 edge cases - unequal or out of bounds or already visited
 if ind == len(word): return true
 recursively perform dfs on the neighbors, ind + 1
 backtrack, 

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m = len(board)
        n = len(board[0])
        ind = 0

        def dfs(i,j, ind):
            # print(i,j,ind)
            if ind == len(word):
                return True
            if i < 0 or i >=m or j < 0 or j >= n or (i,j) in visited or board[i][j] != word[ind]:
                return False
            visited.add((i,j))
            # only need a singular True to be found
            if dfs(i+1, j, ind+1) or dfs(i-1, j, ind+1) or dfs(i, j+1, ind+1) or dfs(i, j-1, ind+1):
                return True
            # the backtracking step!! want to be able to remove from visited so we can see if a better path comes up.
            visited.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[ind]:
                    visited.clear()
                    if dfs(i,j,ind):
                        return True
        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        curr = []
        size = len(word)
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(word_ptr, i, j):
            nonlocal result
            if word_ptr == size - 1:
                result = True
                return
            # recursively check neighbors
            if j + 1 < n and board[i][j+1] == word[word_ptr+1] and (i, j+1) not in visited:
                visited.add((i, j+1))
                dfs(word_ptr+1, i, j+1)
                visited.remove((i, j+1))
            if j - 1 >= 0 and board[i][j-1] == word[word_ptr+1] and (i, j-1) not in visited:
                visited.add((i, j-1))
                dfs(word_ptr+1, i, j-1)
                visited.remove((i, j-1))

            if i + 1 < m and board[i+1][j] == word[word_ptr+1] and (i+1, j) not in visited:
                visited.add((i+1, j))
                dfs(word_ptr+1, i+1, j)
                visited.remove((i+1, j))

            if i - 1 >= 0 and board[i-1][j] == word[word_ptr+1] and (i-1, j) not in visited:
                visited.add((i-1, j))
                dfs(word_ptr+1, i-1, j)
                visited.remove((i-1, j))

            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.clear()
                    visited.add((i,j))
                    dfs(0, i, j)

        return result
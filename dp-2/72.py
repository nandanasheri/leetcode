class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_table = []
        m = len(word1)
        n = len(word2)
        # initialize with zeroes
        for i in range(m+1):
            each = []
            for j in range(n+1):
                each.append(0)
            dp_table.append(each)

        for i in range(m+1):
            dp_table[i][n] = m - i
        for i in range(n+1):
            dp_table[m][i] = n - i
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp_table[i][j] = dp_table[i+1][j+1]
                else:
                    res = min(dp_table[i+1][j], dp_table[i][j+1])
                    res = min(res, dp_table[i+1][j+1])
                    dp_table[i][j] = 1 + res
        
        return dp_table[0][0]
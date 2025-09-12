class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a 2D DP cache m*n
        m = len(text1) 
        n = len(text2) 

        cache = []
        # initialize one extra row and column to prevent out of bounds error
        for i in range(m+1):
            e = []
            for j in range(n+1):
                e.append(0)
            cache.append(e)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # if we have a match add 1 and check diagonal because we can move to next char in both strings
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i+1][j+1]
                # if no match, check 2 subproblems max
                else:
                    cache[i][j] = max(cache[i+1][j], cache[i][j+1])
        
        return cache[0][0]
 


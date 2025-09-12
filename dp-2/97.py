class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp_cache = []

        for i in range(len(s1)+1):
            e = []
            for j in range(len(s2)+1):
                e.append(False)
            dp_cache.append(e)
        
        # It is True that you can interleave empty strings - out of bounds
        dp_cache[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s3[i+j] == s1[i] and dp_cache[i+1][j]:
                    dp_cache[i][j] = True
                if j < len(s2) and s3[i+j] == s2[j] and dp_cache[i][j+1]:
                    dp_cache[i][j] = True
                    
        return dp_cache[0][0]
                   
                
'''
0,0 -> right, down
0,0 -> 0,1
2 decisions to make 
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_cache = []
        for i in range(m+1):
            inner = [0] * (n+1)
            dp_cache.append(inner)

        # one possible way to get to the path from itself
        dp_cache[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                # look right and look down -> those are the two decisions so sum them up
                dp_cache[i][j] = dp_cache[i+1][j] + dp_cache[i][j+1]
        
        return dp_cache[0][0]


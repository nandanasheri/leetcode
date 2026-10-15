'''
     
    [9,9,8,1]
    [5,6,2,6],
    [8,2,6,4],
    [6,2,2,2]

    [0,0]
    [0,0]

    i = 0
'''
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        result = []
        for i in range(n-2):
            x = []
            for j in range(n-2):
                x.append(0)
            result.append(x)
        
        end = 0
        for i in range(0,n-2):
            for j in range(0,n-2):
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        result[i][j] = max(result[i][j], grid[x][y])

        return result

        
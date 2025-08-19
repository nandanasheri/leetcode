class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        start_r, start_c = 0,0
        end_r, end_c = m-1, n-1
        res = []
        direction = 0

        while len(res) != m*n:
            # print(direction, start_r, start_c, end_r, end_c)
            # go right  
            if direction == 0:
                for i in range(start_c, end_c+1):
                    res.append(matrix[start_r][i])
                start_r += 1
            # go down  
            if direction == 1:
                for i in range(start_r, end_r+1):
                    res.append(matrix[i][end_c])
                end_c -= 1
            # go left  
            if direction == 2:
                for i in range(end_c, start_c-1, -1):
                    res.append(matrix[end_r][i])
                end_r -= 1
            # go up 
            if direction == 3: 
                for i in range(end_r, start_r-1, -1):
                    res.append(matrix[i][start_c])
                start_c += 1

            direction = (direction+1) % 4
        return res 
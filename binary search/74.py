# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        m = len(matrix)
        n = len(matrix[0])
        r = (m*n) -1
        while l <= r:
            mid = (l+r) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else: r = mid - 1
        
        return False
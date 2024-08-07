class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        '''
        Recursive DFS solution - recursive function was correct just messed up an if statement
        '''
        start = image[sr][sc]

        def _floodfill (m, n):
            if m < 0 or n < 0 or m >= len(image) or n >= len(image[0]) or image[m][n] != start:
                return
            if image[m][n] == start:
                image[m][n] = color
            
            _floodfill(m+1, n)
            _floodfill(m-1, n)
            _floodfill(m, n+1)
            _floodfill(m, n-1)
        
        if image[sr][sc] == color:
            return image
        _floodfill(sr, sc)
        return image
        
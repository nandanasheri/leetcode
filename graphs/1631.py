class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        visited = set()
        result = float("inf")

        minheap = []
        heapq.heappush(minheap,(0, (0,0)))
        while minheap:
            effort, (i,j) = heapq.heappop(minheap)
            if (i,j) in visited:
                continue
            # we reach target
            if i == m-1 and j == n-1:
                result = min(result, effort)
                continue
            visited.add((i,j))
            for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
                x_i, y_j = x+i, y+j
                if 0 <= x_i < m and 0 <= y_j < n and (x_i, y_j) not in visited:
                   heapq.heappush(minheap,(max(effort, abs(heights[i][j] - heights[x_i][y_j])), (x_i, y_j)))
        
        return result
                
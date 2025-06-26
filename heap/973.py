class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in points:
            x, y = i[0], i[1]
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (distance, i))
        
        result = []
        for i in range(k):
            curr = heapq.heappop(min_heap)[1]
            result.append(curr)
        
        return result
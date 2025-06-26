class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) * -1
            x = heapq.heappop(max_heap) * -1

            if x != y:
                heapq.heappush(max_heap, -(y-x))
        
        if len(max_heap) == 0: return 0
        return max_heap[0] * -1
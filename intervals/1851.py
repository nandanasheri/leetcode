class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        out = {}


        i = 0
        min_heap = []
        
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i+= 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                out[q] = min_heap[0][0]
            else:
                out[q] = -1
            
        res = []
        for i in queries:
            res.append(out[i])
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for i in nums:
            freq_map[i] += 1
        
        max_heap = []
        for key in freq_map:
            max_heap.append((-freq_map[key], key))
        
        heapq.heapify(max_heap)
        result = []
        for i in range(k):
            freq, value = heapq.heappop(max_heap)
            result.append(value)
        
        return result

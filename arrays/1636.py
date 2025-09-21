class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        freq_buckets = defaultdict(list)
        for i in counter:
            freq_buckets[counter[i]].append(i)
        
        min_heap = []
        for i in freq_buckets:
            for j in freq_buckets[i]:
                min_heap.append((i, -j))
        
        heapq.heapify(min_heap)
        print(min_heap)
        result = []

        while min_heap:
            freq, value = heapq.heappop(min_heap)
            for i in range(freq):
                result.append(-value)
        
        return result

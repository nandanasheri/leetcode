class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = []
        counter = defaultdict(int)

        for word in words:
            counter[word] += 1
        
        # switch count to be in first position for the sake of the heap, also negate for max heap
        for key in counter:
            max_heap.append((-counter[key], key))
        
        heapq.heapify(max_heap)

        i = 0
        result = []
        while i < k:
            count, word = heapq.heappop(max_heap)
            result.append(word)
            i += 1
        return result
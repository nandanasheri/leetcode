'''
nums and no sorting - o(nlogn) 
minheap - keeps track in sorted order
nums = [1, 2, 3]
min_heap = [1,2,3]
max_heap [3,2,1]

'''
class MedianFinder:

    def __init__(self):
        # smaller heap is a max heap, larger heap is a min heap
        self.small_heap = []
        self.large_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)

        if self.small_heap and self.large_heap and -self.small_heap[0] > self.large_heap[0]:
            # if largest values in small heap is greater than smallest in large 
            max_val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, max_val)
    
        if len(self.small_heap) - len(self.large_heap) > 1 :
            #  length imbalance, move from small heap to large heap
            max_val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, max_val)
        
        if len(self.large_heap) - len(self.small_heap) > 1:
            min_val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -min_val)
        
    
    def findMedian(self) -> float:
        # print(self.small_heap, self.large_heap)
        if (len(self.small_heap) + len(self.large_heap)) % 2 == 0:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        elif len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        else:
            return self.large_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
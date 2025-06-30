class MedianFinder:

    def __init__(self):
        # array of smaller elements
        self.max_heap = []
        # array of larger elements
        self.min_heap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        # if size imbalance exists, move greatest element to the larger array
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # if greatest elem in small array is mismatched
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
           
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # size mismatch
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        # print(self.max_heap, self.min_heap,)

    def findMedian(self) -> float:
        
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0] ) / 2.0
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
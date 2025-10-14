class HitCounter():
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp:int):
        self.queue.append(timestamp)

    
    def getHits(self, timestamp:int):
        threshold = timestamp - 299
        while self.queue and self.queue[0] < threshold:
            self.queue.popleft()

        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
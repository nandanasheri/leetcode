'''
count within 300 seconds
[1,2,3, 300, 300, 300]
ts = 4 ==> 4
ts = 300 ==> 4
ts = 301 ==> 3
ts = 302 

because time is monotonically increasing - remove any entries 

'''
class HitCounter:

    def __init__(self):
        self.stack = deque()
        
    def hit(self, timestamp: int) -> None:
        self.stack.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        while self.stack and timestamp - self.stack[0] >= 300:
            self.stack.popleft()
        return len(self.stack)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
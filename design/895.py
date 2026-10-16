class FreqStack:

    def __init__(self):
        self.countMap = defaultdict(list)
        self.freqMap = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        # print("In Push", self.countMap, self.freqMap, self.maxCount)
        self.freqMap[val] = self.freqMap.get(val,0) + 1
        self.maxCount = max(self.maxCount, self.freqMap[val])
        self.countMap[self.freqMap[val]].append(val)

    def pop(self) -> int:
        # print("In Pop", self.countMap, self.freqMap, self.maxCount)
        
        val = self.countMap[self.maxCount].pop()
        self.freqMap[val] -= 1
        # no ties, decrement maxCount
        if len(self.countMap[self.maxCount]) == 0:
            self.maxCount -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
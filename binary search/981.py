class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        val = (timestamp, value)
        self.map[key].append(val)

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key not in self.map:
            return value
        l = 0
        r = len(self.map[key]) - 1
        while l <= r:
            mid = (l+r) // 2
            if self.map[key][mid][0] <= timestamp:
                value = self.map[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return value
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
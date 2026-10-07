'''
            lr                   
foo --> [(bar,5), (bar2,10), (bar3,14)]

get(foo, 6)
brute force - linear! o(n) backwards
better than linear get?
binary search with timestamps

'''
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
            return
        self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        l = 0
        r = len(self.time_map[key]) - 1
        result = ""
        while l <= r:
            mid = (l+r) // 2
            if self.time_map[key][mid][0] <= timestamp:
                result = self.time_map[key][mid][1]
                l = mid + 1
            if self.time_map[key][mid][0] > timestamp:
                r = mid - 1
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
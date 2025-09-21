class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.snaps = 0
        self.length = length
        for i in range(length):
            self.arr[i] = [(self.snaps, 0)]

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snaps, val))
        

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1
        

    def get(self, index: int, snap_id: int) -> int:
        all_snaps = self.arr[index]
    
        l, r = 0, len(all_snaps) - 1
        while l <=r:
            mid = (l+r) // 2
            if all_snaps[mid][0] <= snap_id:
                l = mid+1
            else:
                r = mid-1
        # ???? so stupid
        return all_snaps[r][1]
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
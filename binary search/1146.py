'''
[6,0,3]

snap = 1
map that maps the snap_ids to the snapshot {1 : [5,0,0], 2 : [6,0,0]}
{0:{0:5, 1:6}, 1, 2}

'''
class SnapshotArray:

    def __init__(self, length: int):
        self.num_snaps = 0
        self.arr = []
        for i in range(length):
            self.arr.append([(0,0)])
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.num_snaps, val))

    def snap(self) -> int:
        self.num_snaps += 1
        return self.num_snaps - 1
        

    def get(self, index: int, snap_id: int) -> int:
        # print(self.arr)
        l = 0
        r = len(self.arr[index]) - 1
        result = self.arr[index][-1][1]
        while l <= r:
            mid = (l + r) // 2
            if self.arr[index][mid][0] <= snap_id:
                result = self.arr[index][mid][1]
                # want to return right most element in case of duplicate history (most recent)
                l = mid + 1
            else:
                r = mid - 1
        return result


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
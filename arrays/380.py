class RandomizedSet:

    def __init__(self):
        self.randset = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.randset:
            return False
        self.randset[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.randset:
            return False
        ind_remove = self.randset[val]
        # update index position of last element
        last_elem = self.arr[-1]
        self.randset[last_elem] = ind_remove
        # swap elem to remove w the last
        temp = self.arr[ind_remove]
        self.arr[ind_remove] = self.arr[-1]
        self.arr[-1] = temp
        # pop the last elem from both structures
        self.arr.pop()
        self.randset.pop(val)
        return True

    def getRandom(self) -> int:
        rand_ind = random.randint(0, len(self.arr)-1)
        return self.arr[rand_ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
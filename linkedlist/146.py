class Node:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.key, curr.value, end = ";")
            curr = curr.next
        print()
    
    def remove(self, currNode):
        # remove currNode from wherever it is
        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev
        self.map.pop(currNode.key)
    
    def insert(self, currNode):
        self.tail.prev.next = currNode
        currNode.prev = self.tail.prev
        self.tail.prev = currNode
        currNode.next = self.tail
        self.map[currNode.key] = currNode

    def get(self, key: int) -> int:
        # self.print()
        if key in self.map:
            currNode = self.map[key]
            # remove currNode from wherever it is
            self.remove(currNode)
            # move it to the end of cache right behind the tail
            self.insert(currNode)
            return self.map[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # self.print()
        if key in self.map:
            self.remove(self.map[key])
        
         # if at capacity, delete LRU
        if len(self.map) == self.capacity:
            # delete node from the front
            delNode = self.head.next
            self.remove(delNode)
        
        # add a node to the end of the cache - most recently used
        newNode = Node(key, value)
        self.insert(newNode)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
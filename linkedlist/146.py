class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node (0, 0)
        self.tail = Node (0, 0)
        # head - least recent, tail - most recent
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end = "  ")
            curr = curr.next
        print()

    # remove any node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # insert at right
    def insert(self, node):
        previous = self.tail.prev
        previous.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = previous

    def get(self, key: int) -> int:
        # self.print_list()
        if key not in self.map:
            return -1
        self.remove(self.map[key])
        self.insert(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        # self.print_list()
       
        # add to doubly linked list
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key,value)
        self.insert(self.map[key])

        if len(self.map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            self.map.pop(lru.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
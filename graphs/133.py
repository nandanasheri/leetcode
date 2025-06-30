"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = deque()
        hash_map = {}

        if node:
            q.append(node)
            hash_map[node] = Node(node.val)

        while len(q) != 0:
            curr = q.popleft()
            # print(curr.val)
            for each in curr.neighbors:
                if each not in hash_map:
                    hash_map[each] = Node(each.val)
                    q.append(each)
                hash_map[curr].neighbors.append(hash_map[each])
              
        if node in hash_map: return hash_map[node] 
        else: return None
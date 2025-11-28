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
        visited = set()
        clone_map = {}
        q = deque()

        if not node: return None
        # create a start node with no neighbors
        new_node = Node(node.val)
        clone_map [node.val] = new_node
        q.append(node)

        # bfs
        while q:
            curr = q.pop()
            if curr.val in visited:
                continue

            visited.add(curr.val)
            for neighbor in curr.neighbors:
                # print(curr.val, neighbor.val)
                # if a copy doesn't already exist, create the copy
                if neighbor.val not in clone_map:
                    new_node = Node(neighbor.val)
                    clone_map[neighbor.val] = new_node
                # go to the new node's neighbor list and append the new neighbor to it
                clone_map[curr.val].neighbors.append(clone_map[neighbor.val])
                
                # add the original neighbor to the queue
                q.append(neighbor)
        
        return clone_map[node.val]
                


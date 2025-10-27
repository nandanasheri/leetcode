"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
level by level traversal - BFS
queue = [2,3]
while q:
    for each in q:
        curr = 2
        if top exists:
            curr.next = top of the queue 
        if curr.left and curr.right:
        q.append(curr.left)
        q.append(curr.right)

1 -> null
[3, 4, 5]
[4,5,6,7]

2->next = 3

'''

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
            
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            for i in range(q_len):
                curr = q.popleft()
                # if we are at the last element of the current level
                if i != (q_len - 1):
                    curr.next = q[0]
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root
            
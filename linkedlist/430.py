"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = deque()
        curr = head

        if not head:
            return None
        
        # initialize a new head
        res = Node(head.val, None, None, None)
        # move to next node
        if curr.child:
            stack.append(curr)
            curr = curr.child
        else:
            curr = curr.next

        def insert(tail, val):
            tail.next = Node(val, tail, None, None)
            tail = tail.next
        
        new_curr = res
        # end of a level or empty stack
        while curr != None or len(stack):
            # reached end of a level
            if not curr:
                curr = stack.pop().next
            else:
                insert(new_curr, curr.val)
                new_curr = new_curr.next
                if curr.child:
                    stack.append(curr)
                    curr = curr.child
                else:
                    curr = curr.next
        return res
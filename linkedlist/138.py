"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        og_curr = head
        new_head = None
        new_curr = None
        if head == None:
            return None
        
        pointer_arr = {}
        # deep copy of the linked list and next pointers
        while og_curr:
            if new_head == None:
                new_head = Node(og_curr.val)
                new_curr = new_head
            else:
                new_curr.next = Node(og_curr.val)
                new_curr = new_curr.next
            pointer_arr[og_curr] = new_curr
            og_curr = og_curr.next

        # for end of linked list
        pointer_arr[og_curr] = new_curr.next
       
        og_curr = head
        new_curr = new_head
        while og_curr:
            value = og_curr.random
            new_curr.random = pointer_arr[value]
            og_curr = og_curr.next
            new_curr = new_curr.next
        
        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        target_ind = size - n
        ind = 0
        prev = None
        curr = head

        while curr:
            if target_ind == ind:
                if prev:
                    prev.next = curr.next
                    break
                # first node to be removed, move head
                else:
                    head = curr.next
            ind += 1
            prev = curr
            curr = curr.next
        
        return head
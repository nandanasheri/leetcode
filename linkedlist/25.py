# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, k, curr):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kth = self.getKthNode(k, groupPrev)
            # at the end, didn't find a whole k group
            if kth == None:
                break
            
            # reverse k group
            groupNext = kth.next
            curr = groupPrev.next
            prev = kth.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            new_next = groupPrev.next
            groupPrev.next = kth
            groupPrev = new_next
        return dummy.next


            

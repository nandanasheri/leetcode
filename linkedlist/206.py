# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None

        if curr == None:
            return None

        while (curr.next != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = curr
        head.next = prev

        return head
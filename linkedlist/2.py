# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        curr = None
        head = None
        carry = 0

        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            carry = res // 10

            if head == None:
                head = ListNode(res % 10)
                curr = head
            else:
                curr.next = ListNode(res % 10)
                curr = curr.next
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        # in case of unequal sizes
        while curr1:
            res = curr1.val + carry
            carry = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            curr1 = curr1.next
        
        while curr2:
            res = curr2.val + carry
            carry = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            curr2 = curr2.next
        
        if carry != 0:
            curr.next = ListNode(carry)

        return head


        
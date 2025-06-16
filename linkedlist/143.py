# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next == None:
            return
        slow, fast = head, head.next

        # split the list up using slow and fast pointer - slow will be at the end of the first half
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # second is the head of the second half 
        second = slow.next
        slow.next = None

        # reverse the second half of the linked list
        prev = None
        curr = second
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        # merge the two lists together alternatively
        curr1 = head
        curr2 = second
        while curr2 != None:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
            

        
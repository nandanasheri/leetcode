# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        if not curr:
            return None
        while (curr.next != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        head = curr
        return head

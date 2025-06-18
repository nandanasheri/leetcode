# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(list1, list2):
            curr1 = list1
            curr2 = list2
            if curr1 == None:
                return curr2
            if curr2 == None:
                return curr1
            head = None
            if curr1.val < curr2.val:
                head = curr1
                curr1 = curr1.next
            else:
                head = curr2
                curr2 = curr2.next
            curr = head
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next

            if curr1:
                curr.next = curr1
            if curr2:
                curr.next = curr2
            return head
        
        i = 1
        while i < len(lists):
            head = mergeTwoLists(lists[i], lists[i-1])
            lists.remove(lists[i])
            lists.remove(lists[i-1])
            lists.append(head)
        
        if len(lists) == 1: return lists[0]
        else: return None
            

        
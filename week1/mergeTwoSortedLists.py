# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        '''
        here we do the two pointer approach - we also need a head pointer and a new curr pointer to iterate through the new list we're building
        i also used a temp curr pointer probably should've called it temp and make sure to handle the cases where you have leftovers plus empty edge cases
        big o : o(n+m)
        solution online : dummy pointer approach:
        dummy = listnode()
        curr - dummy
        while list1 and list2:
            if compare val:
                curr.next = list1 or list2
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
        that's genius!
        '''
        head = None
        newcurr = None
        curr1 = list1
        curr2 = list2

        # edge cases either empty or both empty
        if curr1 != None and curr2 == None:
            return curr1
        elif curr1 == None and curr2 != None:
            return curr2
        elif curr1 == None and curr2 == None:
            return None

        while (curr1 != None and curr2 != None):
            curr = None
            if curr1.val > curr2.val:
                curr = curr2
                curr2 = curr2.next
            else:
                curr = curr1
                curr1 = curr1.next
            if head == None:
                head = curr
                newcurr = curr
            else:
                newcurr.next = curr
                newcurr = newcurr.next

        if curr1 == None and curr2 != None:
            newcurr.next = curr2
        elif curr1 != None and curr2 == None:
            newcurr.next = curr1

        return head

        
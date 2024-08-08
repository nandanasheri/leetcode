# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        '''
        simple set implementation done it multiple times - pretty simple and standard 
        remember to handle unique values - set is a hastable in python so lookup is o(1) on average
        so o(n) solution
        '''
        curr = head
        visited = set()

        while curr != None:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False

        
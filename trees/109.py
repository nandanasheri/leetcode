# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sorted_nodes = []
        while head:
            sorted_nodes.append(head.val)
            head = head.next
        
        def build_tree(nodes_list):
            if not len(nodes_list):
                return None
            ind = len(nodes_list) // 2
            # print(curr, nodes_list, ind)
            curr = TreeNode(nodes_list[ind])
            curr.left = build_tree(nodes_list[:ind])
            if ind > 0:
                curr.right = build_tree(nodes_list[ind+1:])
            # print(curr)
            return curr
        
        return build_tree(sorted_nodes)
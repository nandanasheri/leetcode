# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            if (not left_tail) and (not right_tail):
                return node
            if not left_tail:
                return left_tail
            else:
                return right_tail
        
        dfs(root)
        
        '''preorder = []

        if not root:
            return
        def preorder_traverse(curr):
            if not curr:
                return
            preorder.append(curr)
            preorder_traverse(curr.left)
            preorder_traverse(curr.right)
        
        preorder_traverse(root)
        
        for i in range(len(preorder)-1):
            curr = preorder[i]
            curr_next = preorder[i+1]
            curr.left = None
            curr.right = curr_next
        
        tail = preorder[-1]
        tail.right = None
        tail.left = None
        return'''
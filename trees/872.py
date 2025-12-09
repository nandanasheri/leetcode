# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq = []
        def inorder_leaves(curr):
            if not curr:
                return
            if not curr.left and not curr.right:
                seq.append(curr.val)
                return
            inorder_leaves(curr.left)
            inorder_leaves(curr.right)
        
        inorder_leaves(root1)
        leaf1 = seq.copy()
        seq.clear()
        inorder_leaves(root2)
        leaf2 = seq.copy()

        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True
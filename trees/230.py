# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def traverse(curr):
            if not curr:
                return
            traverse(curr.left)
            inorder.append(curr.val)
            traverse(curr.right)
        
        traverse(root)
        return inorder[k-1]
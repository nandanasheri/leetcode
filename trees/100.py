# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def _isSame(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if curr1 and curr2 and curr1.val == curr2.val:
                return _isSame(curr1.left, curr2.left) and _isSame(curr1.right, curr2.right)
            else:
                return False
        
        return _isSame(p,q)
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def _isSub(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if curr1 and curr2 and curr1.val == curr2.val:
                return _isSub(curr1.right, curr2.right) and _isSub(curr1.left, curr2.left)
            else:
                return False
        
        if not subRoot:
            return True
        if not root:
            return False
        # only check if subroot and root are actually matching so WORST case will be o(m*n)
        if root and subRoot and root.val == subRoot.val and _isSub(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
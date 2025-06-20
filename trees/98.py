# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minval = float("-infinity")
        maxval = float("infinity")

        def _traverseBST(curr, minval, maxval):
            if not curr:
                return True
            if minval < curr.val < maxval:
                return _traverseBST(curr.left, minval, min(maxval, curr.val)) and _traverseBST(curr.right, max(minval, curr.val), maxval)
            else:
                return False
        return _traverseBST(root, minval, maxval)
        
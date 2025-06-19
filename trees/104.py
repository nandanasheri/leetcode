# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _depth(curr, depth):
            if not curr:
                return depth
            maxL = _depth(curr.left, 1 + depth) 
            maxR = _depth(curr.right, 1 + depth)

            return max(maxL, maxR)
        
        return _depth(root, 0)
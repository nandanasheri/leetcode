# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # this is a global variable that tracks result
        res = 0

        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            maxL = dfs(curr.left)
            maxR = dfs(curr.right)
            res = max(res, maxL + maxR)
            return 1 + max(maxL, maxR)
        
        dfs(root)
        return res

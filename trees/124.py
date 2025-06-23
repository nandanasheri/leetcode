# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxres = root.val

        # return the max path sum without splitting the tree
        def _maxPath(curr):
            nonlocal maxres
            if not curr:
                return 0
            leftMax = _maxPath(curr.left)
            rightMax = _maxPath(curr.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # calculate and update result if you find maximum WITH splitting
            maxres = max(maxres, curr.val + leftMax + rightMax)

            return curr.val + max(leftMax, rightMax)
        
        _maxPath(root)
        return maxres
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def _traverseNodes(curr, max_val):
            nonlocal good
            if not curr:
                return
            if curr.val >= max_val:
                good += 1
            max_val = max(max_val, curr.val)
            _traverseNodes(curr.left, max_val)
            _traverseNodes(curr.right, max_val)
        
        _traverseNodes(root, float("-infinity"))
        return good

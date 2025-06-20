# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root

        def _lca(curr):
            nonlocal res
            if curr == None:
                return
            if (curr.val <= p.val and curr.val >= q.val) or (curr.val >= p.val and curr.val <= q.val):
                res = curr
            elif (curr.val > p.val and curr.val > q.val):
                _lca(curr.left)
            else:
                _lca(curr.right)
        
        _lca(root)
        return res
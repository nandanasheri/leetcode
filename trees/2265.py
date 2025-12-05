# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res_nodes = 0

        def dfs(curr):
            nonlocal res_nodes
            if not curr:
                return (0,0)
            if not curr.left and not curr.right:
                res_nodes += 1
                return (curr.val, 1)
            _left = dfs(curr.left)
            _right = dfs(curr.right)

            avg = (_left[0] + _right[0] + curr.val) // (_left[1] + _right[1] + 1)
            if avg == curr.val:
                res_nodes += 1
            return (_left[0] + _right[0] + curr.val, _left[1] + _right[1] + 1)
        
        dfs(root)
        return res_nodes
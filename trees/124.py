# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_path = float("-inf")

        def dfs(curr):
            nonlocal max_path
            if not curr:
                return 0

            if not curr.left and not curr.right:
                max_path = max(max_path, curr.val)
                return curr.val

            _left_max = dfs(curr.left)
            _right_max = dfs(curr.right)
            
            subtree_max = max([_left_max + _right_max + curr.val, _left_max + curr.val, _right_max + curr.val, curr.val])
            # you can only choose to return a max path not the max subtree
            return_max = max([ _left_max + curr.val, _right_max + curr.val, curr.val])
            max_path = max(max_path, subtree_max)
            
            return return_max
        
        dfs(root)
        return max_path

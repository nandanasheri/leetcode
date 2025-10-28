# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(curr):
            if not curr:
                return None
            # base case we found one of the nodes so we can return that node
            if curr.val == p.val or curr.val == q.val:
                return curr

            l = dfs(curr.left)
            r = dfs(curr.right)

            # if both left and right are not null that means we found p and q as curr's children so return curr
            if l and r:
                return curr
            # we only found left, recursively return left as we backtrack
            if l:
                return l
            if r:
                return r
            return None
        
        return dfs(root)
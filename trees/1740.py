# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        # helper function to find the LCA of both p and q
        def LCA(curr):
            if not curr:
                return None
            if curr.val == p or curr.val == q:
                return curr

            l = LCA(curr.left)
            r = LCA(curr.right)

            if l and r:
                return curr
            if l:
                return l
            if r:
                return r
            return None
        
        def find_dist(start, target, depth):
            if not start:
                return -1
            if start.val == target:
                return depth
            left_depth = find_dist(start.left, target, depth+1)

            if left_depth != -1:
                return left_depth
            else:
                return find_dist(start.right, target, depth+1)

            
            
        lca = LCA(root)
        p_dist = find_dist(lca, p, 0)
        q_dist = find_dist(lca, q, 0)
        return p_dist + q_dist

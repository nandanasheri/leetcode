# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        if not root:
            return []

        def dfs(node, currsum):
            # print(path)
            if not node:
                return
            # we are at a leaf and we find sum
            if not node.left and not node.right and currsum == targetSum:
                res.append(path[::])
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left, currsum+node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, currsum+node.right.val)
                path.pop()
        
        path.append(root.val)    
        dfs(root,root.val)
        return res
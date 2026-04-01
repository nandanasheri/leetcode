# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
curr = [5, 4, 11, 2]
currsum = 22
node = 11
def _traversePath(currsum, curr, node):
    if currsum > target:
        return
    if node is a leaf node:
        currsum += node.val
        if currsum == target:
            curr.append(val)
            result.append(curr[::])
            curr.pop()
        currsum -= node.val
        return

    curr.append(val)
    _traversePath(currsum+node.val, curr, node->left)
    _traversePath(currsum+node.val, curr, node->right)
    curr.pop()
    
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        result = []
        def _traversePath(currsum, curr, node):
            if node == None:
                return
            if node.left == None and node.right == None:
                if currsum + node.val == targetSum:
                    curr.append(node.val)
                    result.append(curr[::])
                    curr.pop()
                return
            curr.append(node.val)
            _traversePath(currsum+node.val, curr, node.left)
            _traversePath(currsum+node.val, curr, node.right)
            curr.pop()
        
        if root == None:
            return []

        _traversePath(0, [], root)
        return result
        
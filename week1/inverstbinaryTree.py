# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        '''
        recursive solution - here we just have one call to the recursive function and we just need to switch the left and right pointers for each curr
        pointer and then recursively work your way down to left and right accordingly 
        big o - o(n) you have to go to each node within the tree
        '''
        def _invertrecur (curr):
            if not curr:
                return
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            _invertrecur(curr.left)
            _invertrecur(curr.right)
        
        if root:
            _invertrecur(root)
        
        return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        I'm bad at binary tree questions - knew it was a post order but didn't realize i need to keep track of two things
        store both height and whether it's balanced within a tuple - don't forget absolute value for difference between heights
        post order traversal - go left, go right, check what is returned then add 1 to max of left and right for height
        '''

        def _balance(curr):
            if curr == None: 
                return (0, True)
            x = _balance(curr.left)
            y = _balance(curr.right)
            isBalanced = x[1] and y[1] and (abs(x[0]-y[0]) <= 1)
            return (1+max(x[0], y[0]), isBalanced)
        
        return _balance(root)[1]